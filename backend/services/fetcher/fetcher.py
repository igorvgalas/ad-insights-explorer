import os
import httpx
import logging
import time
from dotenv import load_dotenv
from typing import List, Dict, Any
from cache.memory_cache import TTLCache


load_dotenv()
fetch_url = os.getenv("FETCH_URL", "https://jsonplaceholder.typicode.com/posts")
max_requests = int(os.getenv("MAX_REQUESTS", 5))

logger = logging.getLogger(__name__)

class PostFetcher:
    def __init__(
        self,
        url: str = fetch_url,
        ttl_seconds: int = 300,
        timeout: float = 5.0,
        max_requests_per_ttl: int = max_requests,
    ):
        self.url = url
        self.cache = TTLCache(ttl_seconds=ttl_seconds)
        self.timeout = timeout
        self.max_requests = max_requests_per_ttl
        self._request_count = 0
        self._ttl_start = time.time()

    def _reset_if_ttl_expired(self):
        if time.time() - self._ttl_start > self.cache.ttl_seconds:
            self._request_count = 0
            self._ttl_start = time.time()

    async def fetch(self) -> List[Dict[str, Any]]:
        self._reset_if_ttl_expired()

        cached = self.cache.get()
        if cached:
            return cached

        if self._request_count >= self.max_requests:
            logger.warning("Max fetch requests exceeded during TTL window. Returning fallback.")
            return cached or []

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(self.url)
                response.raise_for_status()
                posts = response.json()

                if not isinstance(posts, list):
                    raise ValueError("Expected a list of posts")

                self.cache.set(posts)
                self._request_count += 1
                return posts

        except httpx.RequestError as exc:
            logger.error(f"Network error while fetching posts: {exc}")
        except httpx.HTTPStatusError as exc:
            logger.error(f"HTTP error {exc.response.status_code} while fetching posts")
        except ValueError as exc:
            logger.error(f"Failed to parse response: {exc}")
        except Exception as exc:
            logger.exception("Unexpected error while fetching posts")

        return cached or []
