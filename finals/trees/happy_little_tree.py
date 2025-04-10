from __future__ import annotations
from typing import Any, Optional


"""
Bob Ross has decided to retire from painting after one too many incidents with the Titanium White paint ruining his signature afro. He has decided to take up computer science instead, so he sells all his painting supplies - Except his paintbrush, of course - and buys the finest Linux laptop he can find.

Naturally, Ross has taken a liking to the tree data structure in computer science, and has studied it extensively. He has even created his own tree structure, which he calls a Happy Little Tree.

Bob defines a Happy Little Tree as a tree which satisfies the following properties:

There are an even number of subtrees in the tree. Bob does not like it when there are subtrees without a friend :)
All the values within the tree are unique and sum to an odd number.
A Happy Little Tree cannot be empty, because an empty tree is a Sad Little Tree. Bob does not like it when trees are sad and empty.
Bob has asked you to write a method to determine if a given tree is a Happy Little Tree. Help Bob implement this method by completing the is_happy_tree method below.
"""

class Tree:
    """
    Defines a tree.
    """
    def __init__(self, root: Any, subtrees: list[Tree]):
        self.root = root
        self.subtrees = subtrees
    
    def is_happy_tree(self):
        """
        >>> t1 = Tree(1, [Tree(3, []), Tree(2, [])])
        >>> t1.is_happy_tree()
        True
        """
        if self.root is None:
            return False

        def collect_values(tree: Tree) -> list:
            values = [tree.root]
            for subtree in tree.subtrees:
                values.extend(collect_values(subtree))
            return values

        all_values = collect_values(self)

    
        return (sum(all_values) % 2 == 1) and (len(set(all_values)) == len(all_values)) and (len(self.subtrees) % 2 == 0)