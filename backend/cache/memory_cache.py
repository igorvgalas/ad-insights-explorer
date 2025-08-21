import time
from typing import Any, Tuple, Optional


class TTLCache:
    def __init__(self, ttl_seconds: int = 300):
        self.ttl_seconds = ttl_seconds
        self._timestamp: float = 0
        self._value: Any = None
        self._request_count: int = 0

    def _is_valid(self) -> bool:
        return (time.time() - self._timestamp) < self.ttl_seconds

    def get(self) -> Optional[Any]:
        if self._is_valid():
            return self._value
        return None

    def set(self, value: Any):
        self._timestamp = time.time()
        self._value = value
        self._request_count = 0

    def clear(self):
        self._timestamp = 0
        self._value = None
        self._request_count = 0

    def increment_request_count(self):
        """Used to track external fetch calls during the TTL window."""
        if not self._is_valid():
            self._request_count = 0
            self._timestamp = time.time()
        self._request_count += 1

    def get_request_count(self) -> int:
        if not self._is_valid():
            return 0
        return self._request_count
