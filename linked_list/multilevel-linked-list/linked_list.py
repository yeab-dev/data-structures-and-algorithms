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

    def at(self, index) -> Optional[Node]:
        if index < 0:
            raise IndexError(f"Index less than zero ({index})")
        if not self.head:
            return None
        count = 0
        currentNode = self.head
        while index > count:
            if not currentNode:
                raise IndexError(f"Index out of range {index}\n max is {count}")
            count += 1
            currentNode = currentNode.next
        return currentNode