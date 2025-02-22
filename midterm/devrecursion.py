from typing import Any, Optional
# hello1


class _Node:
    """
    Attributes:
        item: Any
        next: Optional[_Node]
    """
    item: Any

    def __init__(self, item: Any) -> None:
        """Initialize a node for a linked list, initially pointing to nothing."""
        self.next = None
        self.item = item

    def __str__(self):
        return str(self.item)

class LinkedList:
    """
    Class for defining a LinkedList.

    Attributes:
        _head: Optional[_Node] 
    """
    _head: Optional[_Node]
    _tail: Optional[_Node]
    _size: int
    
    def __init__(self, items: list[Any]) -> None:
        self._head, self._tail = None, None
        self._size = 0
        for item in items:
            if len(items) == 0:
                self._head = item
            self.append(item)
            self._size += 1

    def to_list(self) -> list:
        items = []
        curr = self._head
        while curr:
            items.append(curr)
            curr = curr.next
        return items

    def append(self, item: Any) -> None:
        if not self._head:
            self._head = _Node(item)
            self._size += 1
        else:
            curr = self._head
            while curr.next:
                curr = curr.next

            curr.next = _Node(item)
            self._size += 1

    def insert(self, index: int, item: Any) -> None:
        """Insert a new node containing item at position <index>.

        Precondition: index >= 0.

        Raise IndexError if index > len(self).

        Note: if index == len(self), this method adds the item to the end
        of the linked list, which is the same as LinkedList.append.

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.insert(2, 300)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200]'
        >>> lst.insert(5, -1)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        """
        if index > self._size:
            raise IndexError
        if index == 0:
            new_node = _Node(item)
            self._head, new_node.next = new_node, self._head
            return
        else:
            curr = self._head
            for _ in range(index-1):
                curr = curr.next
            print(curr)

            new_node = _Node(item)
            curr.next, new_node.next = new_node, curr.next

            print(self)
    
    def pop(self, index: int) -> Any:
        """Remove and return node at position <index>.

        Precondition: index >= 0.

        Raise IndexError if index >= len(self).

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(2)
        10
        >>> lst.pop(0)
        1
        """
        # Warning: the following is pseudo-code, not valid Python code!

        # 1. If the list is empty, you know for sure that index is out of bounds...
        # 2. Else if index is 0, remove the first node and return its item.
        # 3. Else iterate to the (index-1)-th node and update links to remove
        #    the node at position index. But don't forget to return the item!
        if self._size == 0:
            raise IndexError
        elif index == 0:
            temp = self._head.item
            self._head, self._head.next = self._head.next, self._head.next.next
            print(self)
            return temp
        else:
            curr = self._head
            for _ in range(index-1):
                curr = curr.next
            
            temp = curr.next.item
            curr.next = curr.next.next
            print(self)
            return temp
    
    def reverse(self) -> None:
        """
        Reverses the order of the elements in the LinkedList
        """
        curr = self._head
        prev = None

        while curr:
            next = curr.next

            # swap next node and prev
            curr.next, prev = prev, curr
        
            curr = next
        
        self._head = prev
            
    def __str__(self):
        curr = self._head
        items = []
        while curr:
            items.append(curr)
            curr = curr.next
        
        for i in range(len(items)):
            items[i] = items[i].item
        
        return str(items)

if __name__ == "__main__":
    l1 = LinkedList([3,4])
    l1.reverse()
    print(l1)



class Recursion:
    """
    Develop examples of recursion.
    """
    def __init__(self):
        pass

    def factorial(self, num: int) -> int:
        if num < 2:
            return 1
        else:
            return num * self.factorial(num-1)
        
    def fibonacci(self, num: int) -> int:
        if num < 2:
            return 1
        else:
            return self.fibonacci(num-1) + self.fibonacci(num-2)

    def sum_lists(self, lst: list[int]) -> int:
        if len(lst) == 0:
            return 0
        elif len(lst) == 1:
            return 1
        else:
            return lst[0] + self.sum_lists(lst[1:])
    
    def sum_list(self, lst: list) -> int:
        """Returns the sum of list"""
        res = 0
        for i in lst:
            if isinstance(i, list):
                res += self.sum_list(i)
            else:
                res += i
        
        return res
    
    def traverse_linky_recursive(linky: LinkedList) -> None:
        """
        Traverses a linked list recursively and prints out the data of each node
        Precondition:
        linky is a LinkedList
        Note: MAKE MORE TEST CASES!!
        >>> linky = LinkedList([1, 2, 3, 4, 5])
        >>> traverse_linky_recursive(linky)
        1
        2
        3
        4
        5
        """
        curr = linky._head
        if curr:
            print(curr.item)

        

if __name__ == "__main__":
    recurs = Recursion()
    # print(recurs.factorial(3))

    # FIBONACCI

    # for i in range(10):
    #     print(recurs.fibonacci(i), end=' ')

    # SUM LISTS
    # print(recurs.sum_lists([]))
    print(recurs.sum_list([]))