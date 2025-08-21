from collections import defaultdict
from typing import List, Dict, Any
from services.analizer.base import BaseAnomalyDetector
from utils.text import calculate_similarity


class SimilarTitleDetector(BaseAnomalyDetector):
    def __init__(self, posts: List[Dict[str, Any]], threshold: float = 0.8, min_similar: int = 5):
        super().__init__(posts)
        self.threshold = threshold
        self.min_similar = min_similar

    def detect(self) -> List[Dict[str, Any]]:
        user_posts = defaultdict(list)
        for post in self.posts:
            user_posts[post["userId"]].append(post)

        anomalies = []
        for user_id, posts in user_posts.items():
            titles = [post["title"] for post in posts]
            for title in titles:
                similar_count = sum(
                    1 for other in titles
                    if title != other and calculate_similarity(title, other) > self.threshold
                )
                if similar_count >= self.min_similar:
                    anomalies.append({
                        "userId": user_id,
                        "id": None,
                        "title": title,
                        "reason": "Too many similar titles"
                    })
        return anomalies
