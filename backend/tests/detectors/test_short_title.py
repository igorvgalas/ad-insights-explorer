from services.analizer.detectors.short_title import ShortTitleDetector
from tests.testdata.mock_posts import MOCK_POSTS


def test_short_title_detector():
    detector = ShortTitleDetector(MOCK_POSTS)
    anomalies = detector.detect()
    
    assert len(anomalies) == 12
    assert all(len(a["title"]) < 15 for a in anomalies)
    assert all(a["reason"] == "Title too short" for a in anomalies)

