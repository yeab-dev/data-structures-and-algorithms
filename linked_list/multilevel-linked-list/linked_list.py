from typing import Optional
from node import Node
class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
           self.head = newNode
           return
        self.tail.next = newNode
        self.tail = newNode 
