# class Linked:
#     def __init__(self):
#         self.list = []
#
#     def push(self, element, value):
#         self.list.append(element)
#
#     # def next(self, element):
#     #     if
#
# # if __name__ == "__main__":

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
