from typing import List, Optional
from interfaces import Repository

class InMemoryRepository(Repository):
    def __init__(self):
        self._items: List[object] = []

    def add(self, item: object) -> None:
        self._items.append(item)

    def get_by_id(self, item_id: int) -> Optional[object]:
        for item in self._items:
            if getattr(item, "id", None) == item_id:
                return item
        return None

    def get_all(self) -> List[object]:
        return self._items

    def delete(self, item_id: int) -> None:
        item = self.get_by_id(item_id)
        if item:
            self._items.remove(item)