from midterm.stacks.devstack import Stack

def reverse_four(stack: Stack) -> None:
        """
        Given a stack, reverses the last four elements of the stack. If there are less than four elements, the stack should remain unchanged
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.push(4)
        >>> stack.push(5)
        >>> str(stack)
        '5, 4, 3, 2, 1'
        >>> reverse_four(stack)
        >>> str(stack)
        '5, 1, 2, 3, 4'
        """
        if len(stack.items) < 4:
            return
    
        # Pop the top four elements
        temp = [stack.pop() for _ in range(4)]

        # Push them back in reverse order
        for item in temp:
            stack.push(item)

if __name__ == "__main__":
    st = Stack([1,2,3,4])
    reverse_four(st)
    print(st)
            
