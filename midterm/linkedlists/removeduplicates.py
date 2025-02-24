from devll import LinkedList

def remove_duplicates(LL : LinkedList) -> str:
    """Remove duplicated nodes from this linked list.
    The first node of each set of repeated values should be kept.
    Precondition: this linked list is sorted in ascending order.
    >>> LL = LinkedList([1, 2, 2])
    >>> LL.remove_duplicates()
    >>> print(LL)
    [1 -> 2]
    >>> LL = LinkedList([1, 2, 3])
    >>> LL.remove_duplicates()
    >>> print(LL)
    [1 -> 2 -> 3]
    >>> LL = LinkedList([1, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])
    >>> LL.remove_duplicates()
    >>> print(LL)
    [1 -> 2 -> 3 -> 4 -> 5 -> 6]
    """
    curr = LL._head
    pos = curr.next

    while curr and pos:
        if curr.item == pos.item:
            pos = pos.next
        else:
            curr.next = pos
            pos = pos.next
            curr = curr.next
    
    curr.next = None

if __name__ == "__main__":
    import doctest
    doctest.testmod()

            

