import pytest
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient, ASGITransport
from tests.testdata.mock_posts import MOCK_POSTS

@pytest.mark.asyncio
@patch("services.fetcher.fetcher.PostFetcher.fetch", new_callable=AsyncMock)
async def test_get_posts(mock_fetch, client):
    mock_fetch.return_value = MOCK_POSTS

    response = await client.get("/posts")
    assert response.status_code == 200
    assert len(response.json()) == len(MOCK_POSTS)

@pytest.mark.asyncio
@patch("services.fetcher.fetcher.PostFetcher.fetch", new_callable=AsyncMock)
async def test_get_anomalies(mock_fetch, client):
    mock_fetch.return_value = MOCK_POSTS

    response = await client.get("/anomalies")
    assert response.status_code == 200

    anomalies = response.json()
    reasons = {a["reason"] for a in anomalies}
    assert len(anomalies) > 0
    assert "Title too short" in reasons
    assert "Duplicate title" in reasons
    assert "Too many similar titles" in reasons

@pytest.mark.asyncio
@patch("services.fetcher.fetcher.PostFetcher.fetch", new_callable=AsyncMock)
async def test_get_summary(mock_fetch, client):
    mock_fetch.return_value = MOCK_POSTS

    response = await client.get("/summary")
    assert response.status_code == 200

    summary = response.json()
    assert "topUsers" in summary
    assert "commonWords" in summary
    assert isinstance(summary["topUsers"], list)
    assert isinstance(summary["commonWords"], list)
