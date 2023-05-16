from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        else:
            return self.queue.popleft()
