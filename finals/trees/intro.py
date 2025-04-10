from __future__ import annotations
from typing import Any, Optional

class Tree:
    """
    root | Any
    subtrees | list[Tree]
    """
    def __init__(self, root: Any, subtrees: list[Tree]) -> None:
        self.root = root
        self.subtrees = subtrees
    
    def insert(self, item: Any) -> None:
        if self.subtrees:
            self.subtrees[0].insert(item)
        else:
            self.subtrees.append(Tree(item, []))