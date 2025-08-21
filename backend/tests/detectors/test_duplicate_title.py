from services.analizer.detectors.duplicate_title import DuplicateTitleDetector
from tests.testdata.mock_posts import MOCK_POSTS


def test_duplicate_title_detector():
    posts = MOCK_POSTS
    detector = DuplicateTitleDetector(posts)
    anomalies = detector.detect()
    
    assert len(anomalies) >= 1
    assert anomalies[0]["reason"] == "Duplicate title"
    assert anomalies[0]["title"] == "My Post Title"  # ✅ це правильний дублікат у твоїх MOCK_POSTS

