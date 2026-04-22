from typing import Dict, Any, Optional, List


class DataStorage:
    def __init__(self):
        self._records: Dict[int, Dict[str, Any]] = {}
        self._counter = 1

    def create(self, post_data: Dict[str, Any]) -> int:
        item_id = post_data.get("id") or self._counter
        if item_id in self._records:
            item_id = max(self._records.keys() or [0]) + 1

        self._records[item_id] = post_data
        if isinstance(item_id, int) and item_id >= self._counter:
            self._counter = item_id + 1
        return item_id

    def get(self, item_id: int) -> Optional[Dict[str, Any]]:
        return self._records.get(item_id)

    def get_all(self) -> List[Dict[str, Any]]:
        return list(self._records.values())

    def update(self, item_id: int, new_data: Dict[str, Any]) -> bool:
        record = self._records.get(item_id)
        if record is not None:
            record.update(new_data)
            return True
        return False

    def delete(self, item_id: int) -> bool:
        return self._records.pop(item_id, None) is not None
