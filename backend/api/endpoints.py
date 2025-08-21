from fastapi import APIRouter, HTTPException
from services.fetcher.fetcher import PostFetcher
from services.analizer.analyzer import PostAnalyzer
from services.analizer.summary import PostSummary

router = APIRouter()

post_fetcher = PostFetcher()

@router.get("/posts")
async def get_posts():
    try:
        posts = await post_fetcher.fetch()
        return posts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/anomalies")
async def get_anomalies():
    try:
        posts = await post_fetcher.fetch()
        analyzer = PostAnalyzer(posts)
        anomalies = analyzer.detect_anomalies()
        return anomalies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/summary")
async def get_summary():
    try:
        posts = await post_fetcher.fetch()
        summary = PostSummary(posts)
        return summary.generate_summary()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

