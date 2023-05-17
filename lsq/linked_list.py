from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, *nodes_data):
        self.head = None
        if nodes_data is not None:
            deq = deque(nodes_data)
            node = Node(deq.popleft())
            self.head = node
            for elem in deq:
                node.next = Node(elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

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

    def insert(self, node_data):
        node = Node(node_data)
        node.next = self.head
        self.head = node
        return

    def add_last(self, node_data):
        node = Node(node_data)
        if self.head is None:
            self.head = node
            return

        for current_node in self:
            if current_node.next is None:
                current_node.next = node
                return

    def add_before(self, new_node_data, before):
        if self.head is None:
            raise Exception("List is empty")

        elif self.head.data == before:
            self.insert(new_node_data)

        prev_node = self.head
        for node in self:
            if node.data == before:
                new_node = Node(new_node_data)
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

    def add_after(self, new_node_data, after):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == after:
                new_node = Node(new_node_data)
                new_node.next = node.next
                node.next = new_node
                return

    def remove(self, node_to_remove):
        if self.head is None:
            raise Exception("List is empty")

        elif self.head.data == node_to_remove:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == node_to_remove:
                prev_node.next = node.next
                return
            prev_node = node


if __name__ == "__main__":
    linked = LinkedList(1, 2, 3)
    print(linked)

    linked.insert('first')
    print(linked)

    linked.add_last('last')
    print(linked)

    linked.add_before('bruh', 'a')
    print(linked)

    linked.add_after('sus', 'b')
    print(linked)

    linked.remove('c')
    print(linked)

    linked.remove('first')
    print(linked)

    print(len(linked))

