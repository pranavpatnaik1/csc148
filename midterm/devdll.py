from typing import Any, Optional

class _DLLNode:
    """A node in a linked list.
    === Public Attributes ===
    item: The data stored in this node
    next: The next node in the list, or None if there are no further nodes after this node.
    prev: The previous node in the list, or None if there is no node before this one.
    """
    item: Any
    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next or prev node."""
        self.item = item
        self.next = None
        self.prev = None
class CustomDLL:
    """ A customized doubly-linked list. """
    _first: Optional[_DLLNode]
    def __init__(self, lst: list[int]) -> None:
        """Initialize this doubly-linked list."""
        new_lst = []
        for item in lst:
            new_item = _DLLNode(item)
            new_lst.append(new_item)

        # next order
        for i in range(len(new_lst)):
            if i+1 < len(new_lst):
                new_lst[i].next = new_lst[i+1]
        
        # prev order
        reversed_lst = new_lst[::-1]
        for j in range(len(reversed_lst)):
            if j+1 < len(reversed_lst):
                reversed_lst[j].prev = reversed_lst[j+1]
            
        self._first = new_lst[0]

    def __str__(self) -> str:
        curr = self._first
        str_lst = []
        while curr:
            str_lst.append(str(curr.item))
            curr = curr.next
        
        return str(" -> ".join(str_lst))

    def insert_last(self, value: Any, after: Any) -> bool:
        """Insert a new Node with the value <value> after the LAST occurrence of the
        value <after> in this list. If <after> does not exist in the list, then do not
        insert anything and return False.
        The list must be correctly linked after this operation.
        >>> sl = CustomDLL([7, 2, 7, 3])
        >>> str(sl) # You can assume that __str__ is implemented already.
        '7 2 7 3'
        >>> sl.insert_last(5, 7)
        True
        >>> str(sl)
        '7 2 7 5 3'
        >>> sl.insert_last(9, 8)
        False
        >>> str(sl)
        '7 2 7 5 3'
        """
        curr = self._first
        last = None

        while curr:
            if curr.item == after:
                last = curr
            curr = curr.next
        
        if not last:
            return False
        
        next_node = _DLLNode(value)
        next_node.next, next_node.prev = last.next, last
        last.next = next_node
        return True
    

if __name__ == "__main__":
    dll = CustomDLL([1,2,3])
    print(dll)

    print(dll.insert_last(4, 4))
    print(dll)

