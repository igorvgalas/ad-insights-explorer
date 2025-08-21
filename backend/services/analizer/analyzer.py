from typing import List, Dict, Any
from .detectors.short_title import ShortTitleDetector
from .detectors.duplicate_title import DuplicateTitleDetector
from .detectors.similar_title import SimilarTitleDetector


class PostAnalyzer:
    def __init__(self, posts: List[Dict[str, Any]]):
        self.posts = posts
        self.detectors = [
            ShortTitleDetector(posts),
            DuplicateTitleDetector(posts),
            SimilarTitleDetector(posts),
        ]

    def detect_anomalies(self) -> List[Dict[str, Any]]:
        anomalies = []
        for detector in self.detectors:
            anomalies.extend(detector.detect())
        return anomalies
