class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.stack:
            return "the stack is empty"
        else:
            return self.stack.pop()
    def peek(self):
        if not self.stack:
            return "the stack is empty"
        else:
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    