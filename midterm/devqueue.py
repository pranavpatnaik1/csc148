from typing import Any

class Queue:
    """Class for queue implementation.
    
    Attributes:
        items: list[Any]
        top: Any    
    """
    items: list[Any]

    def __init__(self, items):
        self.items = items
    
    def enqueue(self, item: Any) -> None:
        self.items.insert(0, item)
    
    def dequeue(self) -> None:
        self.items, temp = self.items[:-1], self.items[-1]
        return temp
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def peek(self) -> Any:
        return self.items[0]
    
    def __str__(self) -> str:
        return str(self.items)

if __name__ == "__main__":
    queue = Queue([])
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    print(queue)