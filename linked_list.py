class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
    
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