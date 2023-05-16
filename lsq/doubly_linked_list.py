from collections import deque


class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self, nodes_data: deque = None):
        self._nil = _Node('nil')
        self._nil.next = self._nil
        self._nil.prev = self._nil
        try:
            nodes_data.popleft()
        except AttributeError or IndexError:
            self.head = self._nil
        else:
            node = _Node(nodes_data.popleft())
            self.head = node
            for elem in nodes_data:
                node.next = _Node(elem)
                node.prev = node
                node = node.next
            node.next = self._nil
            self._nil.prev = node
            self.head.prev = self._nil
            self._nil.next = self.head

    def __repr__(self):
        node = self.head
        nodes = []
        if node.data == 'nil':
            return "List is empty"

        while node.data != 'nil':
            nodes.append(node.data)
            node = node.next
        return " <-> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length


if __name__ == "__main__":
    linked = DoublyLinkedList(deque(['a', 'b', 'c', 'd']))
    print(linked)
