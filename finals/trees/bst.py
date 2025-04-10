from __future__ import annotations
from typing import Optional, Any

class BinarySearchTree:
    """
    root: Any | None
    left: BinarySearchTree | None
    right: BinarySearchTree | None
    """
    def __init__(self, root: Any | None) -> None:
        """
        Initialize BST.
        """
        if root is None:
            self.root = None
            self.left = None
            self.right = None
        else:
            self.root = root
            self.left = BinarySearchTree(None)
            self.right = BinarySearchTree(None)
    
    def is_empty(self):
        return self.root is None

    def search_item(self, item: Any) -> bool:
        if self.is_empty():
            return False
        elif self.root == item:
            return True
        else:
            if item < self.root:
                return self.left.search_item(item)
            else:
                return self.right.search_item(item)
    
    def insert(self, item: Any) -> None:
        if self.is_empty():
            self.root = item
            self.left = BinarySearchTree(None)
            self.right = BinarySearchTree(None)
        elif item == self.root:
            return
        if item < self.root:
            if not self.left.is_empty():
                self.left.insert(item)
            else:
                self.left = BinarySearchTree(item)
                return
        else:
            if not self.right.is_empty():
                self.right.insert(item)
            else:
                self.right = BinarySearchTree(item)
                return
    
    def delete_item(self, item: Any) -> None:
        if self.is_empty():
            return

        def extract_next(self) -> BinarySearchTree:
            if self.left.is_empty():
                next_node = BinarySearchTree(self.root)
                self.root = None # remove this node
                return next_node
            else:
                return self.left.extract_next()
            
        # Traverse through tree to find item
        if self.root == item:
            # If neither leaf exists
            if self.left.is_empty() and self.right.is_empty():
                self.root = None
            # If one leaf exists
            elif self.left.is_empty():
                self.left, self.right, self.root = \
                    self.right.left, self.right.right, self.right.root
            elif self.right.is_empty():
                self.left, self.right, self.root = \
                    self.left.left, self.left.right, self.left.root
            # If both leaves exist
            else:
                next_node = self.right.extract_next()
                self.root = next_node.root
                
        else:
            if item < self.root:
                self.left.delete_item(item)
            else:
                self.right.delete_item(item)



        
if __name__ == "__main__":
    t1 = BinarySearchTree(1)
    t1.left = BinarySearchTree(2)
    t1.right = BinarySearchTree(3)
    print(t1.search_item(3))