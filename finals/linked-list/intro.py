from __future__ import annotations 
from typing import Any, Optional

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, item: Any) -> None:
        if self.head is None:
            self.head = Node(item)
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = Node(item)
    
    def __str__(self):
        curr = self.head
        ll = []
        while curr:
            ll.append(curr.value)
            curr = curr.next
        
        return str(ll)

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(12)
    print(ll)



    


