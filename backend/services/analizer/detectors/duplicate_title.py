from collections import defaultdict, Counter
from typing import List, Dict, Any
from services.analizer.base import BaseAnomalyDetector


class DuplicateTitleDetector(BaseAnomalyDetector):
    def detect(self) -> List[Dict[str, Any]]:
        user_posts = defaultdict(list)
        for post in self.posts:
            user_posts[post["userId"]].append(post)

        anomalies = []
        for user_id, posts in user_posts.items():
            title_counts = Counter(post["title"] for post in posts)
            for title, count in title_counts.items():
                if count > 1:
                    anomalies.append({
                        "userId": user_id,
                        "id": None,
                        "title": title,
                        "reason": "Duplicate title"
                    })
        return anomalies
