from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self, *nodes_data):
        deq = deque(nodes_data)
        self._nil = Node(None)
        self._nil.next = self._nil
        self._nil.prev = self._nil
        try:
            self.head = Node(deq.popleft())
        except AttributeError or IndexError:
            self.head = self._nil
        else:
            second_node = Node(deq.popleft())
            self.head.next = second_node
            second_node.prev = self.head
            for elem in deq:
                next_node = Node(elem)
                second_node.next = next_node
                next_node.prev = second_node
                second_node = next_node
            second_node.next = self._nil
            self._nil.prev = second_node
            self.head.prev = self._nil
            self._nil.next = self.head

    def __repr__(self):
        node = self.head
        nodes = []
        if node.data is None:
            return "List is empty"

        while node.data is not None:
            nodes.append(str(node.data))
            node = node.next
        return " <-> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node.data is not None:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def remove(self, node_to_remove):
        if self.head is None:
            raise Exception("List is empty")

        else:
            for node in self:
                if node.data == node_to_remove:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    return

    def insert(self, node_data):
        node = Node(node_data)
        node.next = self.head
        node.prev = self._nil
        self.head = node
        return


if __name__ == "__main__":
    linked = DoublyLinkedList(deque([1, 2, 3, 4, 5]))

    linked.remove(3)

    linked.remove(5)

    print(linked)
