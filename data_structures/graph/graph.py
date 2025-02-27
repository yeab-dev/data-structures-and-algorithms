from node import Node
from typing import List
class Graph:
    def __init__(self):
        self.network:List[Node] = []
    
    def add(self, val, neighbors: List[Node]):
        newNode = Node(val, neighbors) 
        if not self.contains(newNode):
            self.network.append(newNode)
    def contains(self, node:Node):
        val = node.val
        neighbors = node.neighbors

        for n in self.network:
            if n.val == val:
                return True
        return False
    def display(self):
        for node in self.network:
            neighbors = ",".join(str(neighbor.val) for neighbor in node.neighbors)
            print(f"{node.val} -> {neighbors if neighbors else 'No Neighbors'}")