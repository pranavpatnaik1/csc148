# How to traverse a binary search tree

# In-order traversal
def in_order_traversal(node):
    if node is None:
        return []
    
    result = []
    
    # First, visit left subtree
    if node.left:
        result.extend(in_order_traversal(node.left))
    
    # Then, visit current node
    result.append(node.value)
    
    # Finally, visit right subtree
    if node.right:
        result.extend(in_order_traversal(node.right))
    
    return result

def post_order_traversal(node):
    if node is None:
        return []
    
    result = []

    if node.left:
        result.extend(post_order_traversal(node.left))

    if node.right:
        result.extend(post_order_traversal(node.right))
    
    result.append(node.value)

    return result