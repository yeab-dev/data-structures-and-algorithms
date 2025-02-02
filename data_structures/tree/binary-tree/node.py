from typing import Any
class Node:
    def __init__(self, val: Any):
        self.val = val
        self.left: Node = None
        self.right: Node = None