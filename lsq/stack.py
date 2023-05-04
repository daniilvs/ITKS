class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return "underflow"
        else:
            return self.stack.pop()

    def top(self):
        return len(self.stack) - 1


if __name__ == "__main__":
    a = Stack()
    a.push(5)
    a.push(66)
    a.push('f')
    a.push(1)
    print(a.top())
    print(a.stack)
    print(a.pop())
    print(a.top())
    print(a.stack)

