from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        currentNode = self.head
        while currentNode:
            print(f"{currentNode.data} ->", end="")
            currentNode = currentNode.next
    def append(self, data):
                
        if not self.head:
            self.head = Node(data)
            return
        lastNode = self.head
        while lastNode:
            if lastNode.next == None:
                lastNode.next = Node(data)
                return
            lastNode = lastNode.next
    
    def delete(self, data):
        currentNode = self.head
        if not currentNode:
           print("the linked list is empty") 
        while currentNode and currentNode.next:
            if currentNode.data == data:
                self.head = currentNode.next
            if currentNode.next.data == data:
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next
    
    def insertAfter(self, key, data):
        currentNode = self.head
        if not currentNode:
            print("the linked list is empty")
            return
        while currentNode and currentNode.next:
            if currentNode.data == key:
                newNode = Node(data)
                newNode.next = currentNode.next
                currentNode.next = newNode
                return
            currentNode = currentNode.next
    def insertAt(self, index, data):
        if index < 0:
            print("invalid index detected")
        count = 0
        currentNode = self.head
        while currentNode and  index >= count:
            if index -1 == count:
                newNode = Node(data)
                newNode.next = currentNode.next
                currentNode.next = newNode
                return
            if currentNode.next == None:
                print("the index you entered is out of range")
            count += 1
            currentNode = currentNode.next