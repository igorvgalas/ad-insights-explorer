import pytest
from httpx import Response
from services.fetcher.fetcher import PostFetcher

@pytest.mark.asyncio
async def test_fetch_success(monkeypatch):
    async def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self): pass
            def json(self): return [{"id": 1, "title": "Hello", "body": "World"}]
        return MockResponse()

    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)
    fetcher = PostFetcher()
    posts = await fetcher.fetch()
    assert isinstance(posts, list)
    assert posts[0]["title"] == "Hello"

@pytest.mark.asyncio
async def test_fetch_network_error(monkeypatch):
    async def mock_get(*args, **kwargs):
        raise Exception("Network error")

    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)
    fetcher = PostFetcher()
    posts = await fetcher.fetch()
    assert posts == []
