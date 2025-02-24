from typing import Any, Optional, Union


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

class LimitedStack:
    """Class for limited stack.
    
    Attributes:
        - _items: list[Any]
        - _size: int
    """
    _items: list[Any]
    _size: int

    def __init__(self, limit: int) -> None:
        """Initialize a limited stack."""
        self._items = []
        self.limit = limit
        self._size = 0
    
    def push(self, value: Any) -> Union[Stack, None]: # type: ignore
        if self._size < self.limit:
            self._items.insert(0, value)
            self._size += 1
    
    def pop(self) -> Any:
        temp = self._items[-1]
        self._items = self._items[1:]
        self._size -= 1
        return temp
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def peek(self) -> Any:
        return self._items[-1]

    def __str__(self) -> str:
        return " ".join(map(str, self._items))

if __name__ == "__main__":
    ls = LimitedStack(4)
    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.pop()
    ls.push(4)
    ls.push(4)
    ls.push(4)
    ls.push(4)
    print(ls)

    