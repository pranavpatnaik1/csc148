from __future__ import annotations
from typing import Any, Optional

class Stack:
    """
    Class for stack, follows LIFO standards.
    """
    def __init__(self) -> None:
        self.stack = []

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Empty stack.")
        else:
            return self.stack.pop()
    
    def push(self, item: Any) -> None:
        self.stack.append(item)
    
    def is_empty(self) -> bool:
        return len(self.stack) == 0


