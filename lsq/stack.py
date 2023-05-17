# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.top = 0
#
#     def push(self, element):
#         self.stack.append(element)
#
#     def pop(self):
#         if len(self.stack) == 0:
#             raise Exception("Stack is empty")
#         else:
#             return self.stack.pop()
#             self.top -= 1
#
#     def top(self):
#         return len(self.queue) - 1
#         self.top += 1
from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.stack = LinkedList()
        self.top = 0

    def __repr__(self):
        node = self.stack.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def pop(self):
        if self.stack.head is None:
            raise Exception("Stack is empty")
        else:
            self.top -= 1
            res = self.stack.head.data
            self.stack.head = self.stack.head.next
            return res

    def push(self, element):
        self.stack.insert(element)
        self.top += 1


if __name__ == "__main__":
    a = Stack()
    a.push(5)
    a.push(66)
    a.push('f')
    a.push(1)
    print(f"top {a.top}")
    print(f"stack {a}")
    print(f"head {a.stack.head.data}")
    print(f"pop {a.pop()}")
    print(f"top {a.top}")
    print(f"stack {a}")
