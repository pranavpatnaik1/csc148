from __future__ import annotations
from typing import Any, List, Optional

"""
Bob defines a Happy Little Tree as a tree which satisfies the following properties:

There are an even number of subtrees in the tree. Bob does not like it when there are subtrees without a friend :)
All the values within the tree are unique and sum to an odd number.
A Happy Little Tree cannot be empty, because an empty tree is a Sad Little Tree. Bob does not like it when trees are sad and empty.
Bob has asked you to write a method to determine if a given tree is a Happy Little Tree. Help Bob implement this method by completing the is_happy_tree method below.
"""

class Tree:
    """
    A tree is a collection of nodes. Each node has a value and a list of subtrees.
    The tree is a recursive data structure.

    value: int
    subtrees: list[Tree]
    """
    def __init__(self, root: Optional[Any], subtrees: list[Tree]):
        self.root = root
        self.subtrees = subtrees

    
    def __len__(self):
        """Return the number of items contained in this tree.
        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        """
        if self.is_empty():
            return 0
        else:
            size = 1
            for subtree in self.subtrees:
                size += subtree.__len__()
            return size

    
    def is_unique(self):
        # UNIQUE VALUES CHECK
        values = []
        for subtree in self.subtrees:
            if subtree.root in values:
                return False
            else:
                values.append(subtree.root)
                subtree.is_unique()
        return True


    def is_happy_tree(self) -> bool:
        """
        Returns whether or not the tree is a Happy Little Tree.
        A Happy Little Tree is a tree which satisfies the following properties:
        - There are an even number of subtrees in the tree. Bob does not like it when there are subtrees without a friend :)
        - All the values within the tree are unique and sum to an odd number.
        - A Happy Little Tree cannot be empty, because an empty tree is a Sad Little Tree. Bob does not like it when trees are sad and empty.

        >>> tree = Tree(1, [])
        >>> tree.is_happy_tree()
        False
        >>> t2 = Tree(1, [Tree(2, []), Tree(3, [])])
        >>> t2.is_happy_tree()
        True
        
        """
        if self.is_empty() or len(self) == 1:
            return False
        elif (len(self) - 1) % 2 == 0 and self.is_unique():
            return True
        else:
            return False
    
    
    def is_empty(self):
        return self.root is None

if __name__ == "__main__":
    import doctest
    doctest.testmod()

