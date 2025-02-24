from devstack import Stack
from devqueue import Queue

def make_queue_from(s: Stack) -> Queue:
    """Clear the Stack s, and return a Queue containing the items that were in s.
    Ensure that when the items are dequeued, the first item that went into the
    original Stack will be the first item out of the Queue.
    >>> nums = Stack([])
    >>> nums.push(1)
    >>> nums.push(2)
    >>> nums.push(3)
    >>> q = make_queue_from(nums)
    >>> nums.is_empty()
    True
    >>> q.enqueue(4)
    >>> q.dequeue()
    1
    >>> q.dequeue()
    2
    >>> q.dequeue()
    3
    >>> q.dequeue()
    4
    >>> q.is_empty()
    True
    """
    temp_stack = Stack([])
    queue = Queue([])
    
    while not s.is_empty():
        temp_stack.push(s.pop())
    
    while not temp_stack.is_empty():
        queue.enqueue(temp_stack.pop())

    return queue

if __name__ == "__main__":
    import doctest
    doctest.testmod() 
