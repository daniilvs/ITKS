class Stack:
    def __init__(self):
        self.stack = []
        self.top = len(self.stack) - 1

    def push(self, element):
        self.stack.append(element)

    def pop(self, element):
        if len(self.stack) == 0:
            return "underflow"
        else:
            return self.stack.pop()
