from node import Node

class LinkedList:
    def __init__(self):
        self.head: Node = None 
        self.tail: Node = None
    def display(self):
        if not self.head:
            print("nothing to show")
            return
        currentNode = self.head
        while currentNode.next:
            if (currentNode == self.tail):
                print(currentNode.data)
                return
            print("{0}<->".format(currentNode.data))
            currentNode = currentNode.next

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
    
    def delete(self, data):
        if not self.head:
            print("not found!")
            return

        currentNode = self.head 
        if currentNode.data == data:
            if currentNode.next == self.head:
                self.head = None
                self.tail = None
                return
            
            currentNode.next.previous = currentNode.previous
            currentNode.previous.next = currentNode.next
            self.head = currentNode.next
            self.tail.next = self.head
            self.head.previous = self.tail
            return
        currentNode = self.tail
        if currentNode.data == data:
            currentNode.previous.next = self.head
            self.head.previous = currentNode.previous
            self.tail = currentNode.previous
            return
        
        currentNode = self.head.next
        while not currentNode.data == data:
            if currentNode.data == data:
                currentNode.previous.next = currentNode.next
                currentNode.next.previous = currentNode.previous
                currentNode = None
                return
            currentNode = currentNode.next
        
        print("{0} was not found in the list".format(data))
    
    def indexOf(self, data) -> int:
        if not self.head:
            return -1
        currentNode = self.head
        count = 0
        while not currentNode == self.tail and not currentNode.data == data:
            currentNode = currentNode.next
            count += 1
        if currentNode.data == data:
            return count
        return -1
    
    def insertAfter(self, data, newData):
        if not self.head:
            print("the list is empty")
            return        
        currentNode = self.head
        newNode = Node(newData)
        if self.tail.data == data:
            self.tail.next.previous = newNode
            newNode.previous = self.tail
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
            return
        while not currentNode.data == data:
            currentNode = currentNode.next
            if currentNode == self.head:
               print("{0} not found in the list".format(data))
               return 
        
        newNode.next = currentNode.next
        newNode.previous = currentNode
        newNode.next.previous = newNode
        currentNode.next = newNode
    def size(self):
        if not self.head:
            return 0
        currentNode = self.head
        size = 1
        while not currentNode == self.tail:
            currentNode = currentNode.next
            size += 1
