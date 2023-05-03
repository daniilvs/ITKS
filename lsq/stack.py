class Stack():
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack[0] = element

    def pop(self, element):
        return self.stack.pop(0)
