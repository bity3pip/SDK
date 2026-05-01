import os

import requests

from app.schemas.post import PostRead

BASE_URL = os.getenv('BASE_URL', 'https://jsonplaceholder.typicode.com')


class JSONPlaceholderSDK:
    def __init__(self) -> None:
        self.BASE_URL = BASE_URL

    def get_post(self, post_id: int) -> PostRead:
        response = requests.get(f"{self.BASE_URL}/posts/{post_id}")
        response.raise_for_status()
        return PostRead.model_validate(response.json())

    def get_all_posts(self, limit: int = 5) -> list[PostRead]:
        response = requests.get(f"{self.BASE_URL}/posts")
        response.raise_for_status()
        return [PostRead.model_validate(post) for post in response.json()[:limit]]

    def create_post(self, title: str, body: str, user_id: int) -> PostRead:
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(f"{self.BASE_URL}/posts", json=payload)
        response.raise_for_status()
        return PostRead.model_validate(response.json())
