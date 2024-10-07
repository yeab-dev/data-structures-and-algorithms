class Node:
    def __init__(self, data):
        self.previous:Node = None
        self.next: Node = None
        self.data = data