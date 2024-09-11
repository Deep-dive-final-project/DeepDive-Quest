from redis import Redis
import json


class QuestCache:
    def __init__(self):
        self.cache = Redis(host='localhost', port=6379, db=1)

    def get_quest(self, key: str) -> str | None:
        redis_key = f"fastapi:quest:key={key}"
        cached_data: str = self.cache.get(redis_key)
        if cached_data:
            return cached_data
        return None

    def save_quest(self, key: str, val: str):
        redis_key = f"fastapi:quest:key={key}"
        self.cache.set(redis_key, val)
