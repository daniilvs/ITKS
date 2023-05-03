class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self, element):
        if len(self.queue) == 0:
            return "underflow"
        else:
            return self.queue.pop(0)
