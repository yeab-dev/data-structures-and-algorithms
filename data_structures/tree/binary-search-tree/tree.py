from node import Node
from typing import Any, List
class Tree:
    def __init__(self):
        self.root = None
    
    def _in_order_traversal(self, node: Node, result: List[Any]):
        if not node:
            return
        else:
            self._in_order_traversal(node.left, result)
            result.append(node.val)
            self._in_order_traversal(node.right, result)
    
    def sort(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result
    
    def insert(self, val: Any): 
        newNode = Node(val= val)
        if not self.root:
            self.root = newNode
            return
        node = self.root
        while True:
            if newNode.val > node.val:
                if not node.right:
                    node.right = newNode
                    return
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = newNode
                    return
                else:
                    node = node.left
    def find_min(self, node: Node):
        while node.left:
            node = node.left
        return node 
    def delete(self, root: Node, val: Any):
        if not root:
            return None
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if not (root.left or root.right):
                return None
            elif (root.left is None):
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min(root.right)
                root.val = successor.val
                root.right = self.delete(root.right, successor.val)