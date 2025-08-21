from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseAnomalyDetector(ABC):
    def __init__(self, posts: List[Dict[str, Any]]):
        self.posts = posts

    @abstractmethod
    def detect(self) -> List[Dict[str, Any]]:
        pass