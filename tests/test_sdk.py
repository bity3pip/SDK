from typing import Any
from unittest.mock import MagicMock

from app.service.post_service import PostService
from app.storage.memory_storage import DataStorage


class TestPostSDK:
    def test_storage_crud(self, storage: DataStorage) -> None:
        post_data: dict[str, Any] = {"id": 1, "title": "test"}
        item_id = storage.create(post_data)
        assert item_id == 1

        saved_item = storage.get(1)
        assert saved_item is not None
        assert saved_item["title"] == "test"

        storage.update(1, {"title": "updated"})
        updated_item = storage.get(1)
        assert updated_item is not None
        assert updated_item["title"] == "updated"

        storage.delete(1)
        assert storage.get(1) is None

    def test_service_fetch_and_save(self, service: PostService, storage: DataStorage) -> None:
        mock_post: dict[str, Any] = {
            "id": 5,
            "title": "Mock Post",
            "body": "content",
            "userId": 1,
        }
        service.sdk.get_post = MagicMock(return_value=mock_post)  # type: ignore

        fetched_post = service.fetch_and_save_post(5)

        assert fetched_post["id"] == 5
        assert len(storage.get_all()) == 1
        post = storage.get(5)
        assert post is not None
        assert post["title"] == "Mock Post"
