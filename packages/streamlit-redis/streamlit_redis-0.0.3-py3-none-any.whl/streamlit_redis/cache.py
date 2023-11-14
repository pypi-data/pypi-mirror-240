from __future__ import annotations

import uuid

from streamlit.runtime.caching.storage import (
    CacheStorage,
    CacheStorageContext,
    CacheStorageError,
    CacheStorageKeyNotFoundError,
    CacheStorageManager,
)
from streamlit.logger import get_logger
from streamlit.runtime.secrets import secrets_singleton
import redis

_LOGGER = get_logger(__name__)


class RedisCacheStorageManager(CacheStorageManager):
    @classmethod
    def from_secrets(cls):
        secrets_singleton.load_if_toml_exists()
        redis_dsn = secrets_singleton["streamlit_redis"]["dsn"]
        try:
            app_prefix = secrets_singleton["streamlit_redis"]["app_prefix"]
        except KeyError:
            app_prefix = str(uuid.uuid4())
        return cls(redis_dsn, app_prefix)

    def __init__(self, dsn: str, app_prefix):
        self.dsn: str = dsn
        self.app_prefix: str = app_prefix
        self.redis_client: redis.Redis = redis.from_url(dsn)

    def create(self, context: CacheStorageContext) -> CacheStorage:
        """Creates a new cache storage instance"""
        try:
            self.redis_client.ping()
        except Exception as e:
            # TODO: raise a more specific exception here
            raise e

        return RedisCacheStorage(
            context=context,
            redis_client=self.redis_client,
            app_prefix=self.app_prefix
        )

    def clear_all(self) -> None:
        self.redis_client.delete(*self.redis_client.keys(f"{self.app_prefix}:*"))

    def check_context(self, context: CacheStorageContext) -> None:
        if context.persist == "disk":
            _LOGGER.warning(
                f"The cached function '{context.function_display_name}' has a persist='disk' "
                "that will be ignored. RedisCacheStorageManager currently doesn't support persist option."
            )


class RedisCacheStorage(CacheStorage):
    """Cache storage protocol, that should be implemented by the concrete cache storages.
    Used to store cached values for a single `@st.cache_data` decorated function
    serialized as bytes.

    CacheStorage instances should be created by `CacheStorageManager.create()` method.

    Notes
    -----
    Threading: The methods of this protocol could be called from multiple threads.
    This is a responsibility of the concrete implementation to ensure thread safety
    guarantees.
    """

    def __init__(self, context: CacheStorageContext, redis_client: redis.Redis, app_prefix: str):
        self.function_key = context.function_key
        self.function_display_name = context.function_display_name
        self._ttl_seconds = context.ttl_seconds
        self.app_prefix = app_prefix
        self.redis_client = redis_client

    def make_redis_key(self, suffix) -> str:
        return ":".join((self.app_prefix, self.function_key, suffix))

    def get(self, key: str) -> bytes:
        """Returns the stored value for the key.

        Raises
        ------
        CacheStorageKeyNotFoundError
            Raised if the key is not in the storage.
        """
        try:
            redis_key = self.make_redis_key(key)
            result = self.redis_client.get(redis_key)
            if result is None:
                raise Exception("Key not found in redis cache")
            return result
        except Exception:
            raise CacheStorageKeyNotFoundError("Key not found in redis cache")

    def set(self, key: str, value: bytes) -> None:
        """Sets the value for a given key"""
        redis_key = self.make_redis_key(key)
        try:
            self.redis_client.set(redis_key, value, ex=self._ttl_seconds)
        except Exception as e:
            raise CacheStorageError("Error while setting key in redis cache") from e

    def delete(self, key: str) -> None:
        """Delete a given key"""
        redis_key = self.make_redis_key(key)
        try:
            self.redis_client.delete(redis_key)
        except Exception:
            raise CacheStorageError("Error while deleting key in redis cache")

    def clear(self) -> None:
        """Remove all keys for the storage"""
        redis_key_pattern = self.make_redis_key("*")
        try:
            self.redis_client.delete(*self.redis_client.keys(redis_key_pattern))
        except Exception:
            raise CacheStorageError("Error while clearing redis cache")
