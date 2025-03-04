from typing import Any

class Queue:
    """Class for queue implementation.
    
    Attributes:
        items: list[Any]
        top: Any    
    """
    items: list[Any]

    def __init__(self, items: list[Any]):
        self.items = items
    
    def enqueue(self, item: Any) -> None:
        self.items.append(item)
    
    def dequeue(self) -> None:
        return self.items.pop(0)
    
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