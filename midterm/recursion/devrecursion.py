from typing import Any, Optional
import doctest


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

            new_node = _Node(item)
            curr.next, new_node.next = new_node, curr.next
    
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
            return temp
        else:
            curr = self._head
            for _ in range(index-1):
                curr = curr.next
            
            temp = curr.next.item
            curr.next = curr.next.next
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

    def print_helper(self, node: _Node) -> Any:
        if node:
            print(node.item)
            self.print_helper(node.next)
    
    def traverse_linky_recursive(self, linky: LinkedList) -> None:
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
        self.print_helper(curr)
    
    def is_power(self, x: int, y: int) -> bool:
        """
        Returns true iff x is a power of y, False otherwise
        Precondition:
        x and y are positive non-zero integers
        >>> is_power(8, 2)
        True
        >>> is_power(9, 2)
        False
        >>> is_power(1, 1)
        True
        """
        if y == 1:
            return x == 1
        if x < y:
            return False
        elif x == y or x % y != 0:
            return True
        else:
            return self.is_power(x/y,y) # type: ignore
    
    def weave_lists_recursive(self, linky1: LinkedList, linky2: LinkedList) -> LinkedList:
        """
        Merges two linked lists into a single linked list, maintaining the sorted order
        Precondition:
        linky1 and linky2 are sorted in ascending order
        Note: MAKE MORE TEST CASES! (Especially edge cases)
        >>> linky1 = LinkedList([1, 3, 5])
        >>> linky2 = LinkedList([2, 4, 6])
        >>> weave_lists_recursive(linky1, linky2)
        1 -> 2 -> 3 -> 4 -> 5 -> 6
        """
        def merge_recursive(node1: _Node, node2: _Node) -> LinkedList:
            if not node1:
                return node2
            if not node2:
                return node1
            
            if node1.item < node2.item:
                node1.next = merge_recursive(node1.next, node2)
                return node1
            else:
                node2.next = merge_recursive(node1, node2.next)
                return node2

        merged_list = LinkedList([])
        merged_list._head = merge_recursive(linky1._head, linky2._head) # type: ignore
        return merged_list

    def pascal_r(self, n: int) -> list[list[int]]:
        """
        Returns the first n rows of Pascal's Triangle
        Precondition:
        n >= 0
        >>> pascal_r(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        """
        if n == 0:
            return []

        res = [[1]]
        if n == 1:
            return res

        def helper(lst: list[int]) -> list[int]:
            temp = [1]  # First element is always 1
            for i in range(len(lst) - 1):
                temp.append(lst[i] + lst[i + 1])  # Sum of adjacent elements
            temp.append(1)  # Last element is always 1
            return temp

        for _ in range(n - 1):  # Start from 1 since we already have the first row
            res.append(helper(res[-1]))

        return res

    def ispalindrome(self, s: str) -> bool:
        """Return whether <s> is a palindrome.
        The function must be implemented **recursively**.
        """
        if len(s) == 0:
            return True
        
        if s[0] == " ":
            return self.ispalindrome(s[1:])
        elif s[-1] == " ":
            return self.ispalindrome(s[:-1])
        if s[0] == s[-1]:
            return self.ispalindrome(s[1:-1])
        else:
            return False


if __name__ == "__main__":
    recurs = Recursion()
    # print(recurs.factorial(3))

    # FIBONACCI

    # for i in range(10):
    #     print(recurs.fibonacci(i), end=' ')

    # SUM LISTS
    # print(recurs.sum_lists([]))
    # print(recurs.sum_list([]))
    # recurs.traverse_linky_recursive(LinkedList([1,2,3,4,5]))
    # print(recurs.is_power(9, 2))
    # print(recurs.weave_lists_recursive(LinkedList([1, 3, 5]), LinkedList([2, 4, 6])))
    # print(recurs.pascal_r(5))

    print(recurs.ispalindrome("borrow or rob"))

    