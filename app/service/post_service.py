from app.schemas.post import PostRead
from app.sdk.jsonplaceholder import JSONPlaceholderSDK
from app.storage.memory_storage import DataStorage


class PostService:
    def __init__(self, sdk: JSONPlaceholderSDK, storage: DataStorage):
        self.sdk = sdk
        self.storage = storage

    def get_post(self, post_id: int) -> PostRead:
        local_post = self.storage.get(post_id)
        if local_post:
            return local_post

        post_data = self.sdk.get_post(post_id)
        self.storage.create(post_data)
        return post_data

    def get_recent_posts(self, limit: int = 5) -> list[PostRead]:
        posts = self.sdk.get_all_posts(limit=limit)
        for post in posts:
            self.storage.create(post)
        return posts

    def create_post(self, title: str, body: str, user_id: int) -> PostRead:
        post_data = self.sdk.create_post(title, body, user_id)
        self.storage.create(post_data)
        return post_data

    def get_local_posts(self) -> list[PostRead]:
        return self.storage.get_all()
