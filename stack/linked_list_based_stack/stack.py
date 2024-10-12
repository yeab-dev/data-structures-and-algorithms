from node import Node
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
    
    def push(self, data):
        newNode = Node(data)
        if not self.top:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.count += 1
    def pop(self):
        if not self.top:
            return "the stack is empty"
        else:
            temp = self.top
            self.top = temp.next
            self.count -= 1
            return temp.valuet 