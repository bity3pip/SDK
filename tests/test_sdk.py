import unittest
from unittest.mock import MagicMock
from app.sdk.jsonplaceholder import JSONPlaceholderSDK
from app.service.post_service import PostService
from app.storage.memory_storage import DataStorage


class TestSDKTask(unittest.TestCase):
    def setUp(self):
        self.sdk = JSONPlaceholderSDK()
        self.storage = DataStorage()
        self.service = PostService(self.sdk, self.storage)

    def test_storage_crud(self):
        post_data = {"id": 1, "title": "test"}
        item_id = self.storage.create(post_data)
        self.assertEqual(item_id, 1)

        saved_item = self.storage.get(1)
        self.assertEqual(saved_item["title"], "test")

        self.storage.update(1, {"title": "updated"})
        self.assertEqual(self.storage.get(1)["title"], "updated")

        self.storage.delete(1)
        self.assertIsNone(self.storage.get(1))

    def test_service_fetch_and_save(self):
        mock_post = {
            "id": 5,
            "title": "Mock Post",
            "body": "content",
            "userId": 1,
        }
        self.service.sdk.get_post = MagicMock(return_value=mock_post)

        fetched_post = self.service.fetch_and_save_post(5)

        self.assertEqual(fetched_post["id"], 5)
        self.assertEqual(len(self.storage.get_all()), 1)
        self.assertEqual(self.storage.get(5)["title"], "Mock Post")
