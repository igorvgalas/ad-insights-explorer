from collections import Counter, defaultdict
from typing import List, Dict, Any


class PostSummary:
    def __init__(self, posts: List[Dict[str, Any]]):
        self.posts = posts

    def generate_summary(self) -> Dict[str, Any]:
        return {
            "topUsers": self._get_top_users(),
            "commonWords": self._get_common_words()
        }

    def _get_top_users(self, top_n: int = 3) -> List[Dict[str, Any]]:
        user_words = defaultdict(set)
        for post in self.posts:
            words = set(post['title'].split())
            user_words[post['userId']].update(words)

        sorted_users = sorted(user_words.items(), key=lambda x: len(x[1]), reverse=True)
        return [{"userId": user_id, "uniqueWords": len(words)} for user_id, words in sorted_users[:top_n]]

    def _get_common_words(self, top_n: int = 10) -> List[tuple]:
        all_words = Counter(
            word.lower()
            for post in self.posts
            for word in post['title'].split()
        )
        return all_words.most_common(top_n)
