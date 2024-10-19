from linked_list import linked_list 
class Queue:
    def __init__(self):
        self.queue = linked_list.LinkedList()
    
    def enqueue(self, val):
        self.queue.append(val)
    def dequeue(self):
        if not self.queue.head:
            raise IndexError("Cannot dequeue from an empty queue")
        if self.queue.head == self.queue.tail:
            nodeToRemove = self.queue.head
            self.queue.head = None
            self.queue.tail = None
            return nodeToRemove.data
        nodeToRemove = self.queue.head
        self.queue.tail.next = self.queue.head.next
        self.queue.head = self.queue.head.next
        self.queue.head.previous = self.queue.tail
        return nodeToRemove.data
    def peek(self):
        if not self.queue.head:
            raise IndexError("Empty queue")
        return self.queue.head.data
