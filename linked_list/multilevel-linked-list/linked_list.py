class LinkedList:
    def __init__(self):
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
           self.head = newNode
           return
        self.tail.next = newNode
        self.tail = newNode 
