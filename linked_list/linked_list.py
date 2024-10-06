from node import Node

class LinkedList:
    def __init__(self):
        self.head: Node = None 
        self.tail: Node = None
    def append(self, data):
        newNode = Node(data)
        if not self.head:
           self.head = newNode
           self.tail = newNode
           newNode.next = newNode
           newNode.previous = newNode
           return
        newNode.next = self.head
        newNode.previous = self.tail
        self.head.previous = newNode
        self.tail.next = newNode
        self.tail = newNode
    def prepend(self, data):
        newNode = Node(data)
        if not self.head:
           self.head = newNode
           self.tail = newNode
           self.head.previous = self.tail
           self.tail.next = self.head
           return
        newNode.next = self.head
        newNode.previous = self.tail
        self.head.previous = newNode
        self.tail.next = newNode
        self.head = newNode
