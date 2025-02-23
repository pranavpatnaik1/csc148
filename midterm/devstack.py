from typing import Any, Optional
from devexception import EmptyStackException

class Stack:
    """
    Attributes:
        items: list[Any]
        top: Any
    """
    items: list[Any]
    top: Any
    
    def __init__(self, items: list[Any]) -> None:
        self.items = items
        self.top = None

    def push(self, item: Any) -> None:
        self.items.append(item)
    
    def pop(self) -> Any:
        if self.is_empty():
            raise EmptyStackException
        self.items, temp = self.items[:-1], self.items[-1]
        return temp
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def peek(self) -> Any:
        return self.items[-1]
    
    def __str__(self) -> list[Any]:
        return str(self.items)


if __name__ == "__main__":
    stack = Stack([1])
    stack.pop()
    stack.pop()

    

