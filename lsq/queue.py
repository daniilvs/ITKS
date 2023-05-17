from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def __repr__(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        else:
            res = [str(i) for i in self.queue]
            return " <- ".join(res)

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        else:
            return self.queue.popleft()
# from linked_list import LinkedList
#
#
# class Queue:
#     def __init__(self):
#         self.queue = LinkedList()
#         self.tail = None
#
#     def __repr__(self):
#         node = self.queue.head
#         nodes = []
#         while node is not None:
#             nodes.append(str(node.data))
#             node = node.next
#         return " -> ".join(nodes)
#
#     def enqueue(self, element):
#         self.queue.insert(element)
#         self.tail = element
#
#     def dequeue(self):
#         self.tail -= 1
#         return self.queue.remove(self.tail)


if __name__ == "__main__":
    a = Queue()
    a.enqueue(5)
    a.enqueue(66)
    a.enqueue('f')
    a.enqueue(1)
    print(f"queue {a}")
    # print(f"head {a.queue.head.data}")
    print(f"dequeue {a.dequeue()}")
    # print(f"tail {a.tail}")
    print(f"queue {a}")
