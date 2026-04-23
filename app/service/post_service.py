from typing import Any, Dict, List

from app.sdk.jsonplaceholder import JSONPlaceholderSDK
from app.storage.memory_storage import DataStorage


class PostService:
    def __init__(self, sdk: JSONPlaceholderSDK, storage: DataStorage):
        self.sdk = sdk
        self.storage = storage

    def fetch_and_save_post(self, post_id: int) -> Dict[str, Any]:
        local_post = self.storage.get(post_id)
        if local_post:
            return local_post

        post_data = self.sdk.get_post(post_id)
        self.storage.create(post_data)
        return post_data

    def fetch_and_save_recent_posts(self, limit: int = 5) -> List[Dict[str, Any]]:
        posts = self.sdk.get_all_posts(limit=limit)
        for post in posts:
            self.storage.create(post)
        return posts

    def create_remote_and_local_post(self, title: str, body: str, user_id: int) -> Dict[str, Any]:
        post_data = self.sdk.create_post(title, body, user_id)
        self.storage.create(post_data)
        return post_data

    def get_local_posts(self) -> List[Dict[str, Any]]:
        return self.storage.get_all()
