class Tree:
    """
    A tree is a collection of nodes. Each node has a value and a list of subtrees.
    The tree is a recursive data structure.

    value: int
    subtrees: list[Tree]
    """
    def __init__(self, value):
        self.value = value
        self.subtrees = []
