from __future__ import annotations
from typing import Any

class Queue:
    """
    Class for queue. Follows FIFO standards.
    """
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, item: Any) -> None:
        self.queue.append(item)
    
    def dequeue(self) -> Any:
        return self.queue.pop(0)
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0
    