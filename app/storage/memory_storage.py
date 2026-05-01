from typing import Any, Dict

from app.schemas.post import PostRead


class DataStorage:
    def __init__(self) -> None:
        self._records: Dict[int, PostRead] = {}
        self._counter = 1

    def create(self, post_data: PostRead) -> int:
        item_id = post_data.id or self._counter
        if item_id in self._records:
            item_id = max(self._records.keys() or [0]) + 1

        self._records[item_id] = post_data
        if item_id >= self._counter:
            self._counter = item_id + 1
        return item_id

    def get(self, item_id: int) -> PostRead | None:
        return self._records.get(item_id)

    def get_all(self) -> list[PostRead]:
        return list(self._records.values())

    def update(self, item_id: int, new_data: Dict[str, Any]) -> bool:
        record = self._records.get(item_id)
        if record is not None:
            self._records[item_id] = record.model_copy(update=new_data)
            return True
        return False

    def delete(self, item_id: int) -> bool:
        return self._records.pop(item_id, None) is not None
