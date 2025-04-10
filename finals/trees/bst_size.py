from __future__ import annotations
from typing import Any


class Tree:
    """
    root: Any
    subtrees: list[Tree]
    """
    def __init__(self, root: Any, subtrees: list[Tree]):
        self.root = root
        self.subtrees = subtrees
    
    def find_size(self) -> int:
        size = 1  # Count the current root node

        for subtree in self.subtrees:
            size += subtree.find_size()

        return size

    def delete_item(self, item: Any) -> bool:
        if self.root is None:
            return False
        elif not self.subtrees: # leaf case
            if self.root == item:
                self.root = None
                return True
            else:
                return False
        else:
            if self.root == item:
                replacement = self.subtrees.pop()
                self.root = replacement.root
                self.subtrees.extend(replacement.subtrees)
                return True
            else:
                for subtree in self.subtrees:
                    deleted = subtree.delete_item(item)
                    if deleted:
                        return True
        
        return False
    
    def __str__(self):
        # res = f"{self.root}\n"
        # if self.root is None:
        #     return ""
        # for subtree in self.subtrees:
        #     res += str(subtree)
        
        # return res
        return self.str_indented(0)

    def str_indented(self, depth:int):
        res = " " * depth + f"{self.root}" + "\n"
        if self.root is None:
            return ""
        for subtree in self.subtrees:
            res += subtree.str_indented(depth + 1)
        
        return res

if __name__ == "__main__":
    t1 = Tree(1, [Tree(2, []), Tree(3, [])])
    print(t1)



        


