from services.analizer.detectors.similar_title import SimilarTitleDetector
from tests.testdata.mock_posts import MOCK_POSTS

def test_similar_title_detector():
    posts = MOCK_POSTS
    detector = SimilarTitleDetector(posts)
    anomalies = detector.detect()

    # At least one should be triggered
    assert any(a["reason"] == "Too many similar titles" for a in anomalies)
    assert any(a["userId"] == 1 for a in anomalies)
