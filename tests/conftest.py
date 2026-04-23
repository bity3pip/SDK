import pytest

from app.sdk.jsonplaceholder import JSONPlaceholderSDK
from app.service.post_service import PostService
from app.storage.memory_storage import DataStorage


@pytest.fixture
def sdk() -> JSONPlaceholderSDK:
    return JSONPlaceholderSDK()


@pytest.fixture
def storage() -> DataStorage:
    return DataStorage()


@pytest.fixture
def service(sdk: JSONPlaceholderSDK, storage: DataStorage) -> PostService:
    return PostService(sdk, storage)
