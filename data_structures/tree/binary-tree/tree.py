from node import Node
from typing import Any
class Tree:
    def __init__(self):
        self.root = None
    
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