from typing import List, Dict, Any
from services.analizer.base import BaseAnomalyDetector


class ShortTitleDetector(BaseAnomalyDetector):
    def detect(self) -> List[Dict[str, Any]]:
        return [
            {
                "userId": post["userId"],
                "id": post["id"],
                "title": post["title"],
                "reason": "Title too short"
            }
            for post in self.posts
            if len(post["title"]) < 15
        ]
