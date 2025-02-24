from typing import Any, Optional

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
    
        

