class Node:
    """Creates node. Node contains information about data which is put in it and
    pointers to the next (for both linked list and doubly linked list) and to the 
    previous (only for doubly linked list) nodes in list"""

    def __init__(self, data):
        """Node constructor"""
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        """String representation"""
        return str(self.data)

    def __eq__(self, other):
        return str(self) == str(other)

    def put_next(self, node):
        """(only for doubly linked list) puts node from filter
        ahead of the self one"""
        self.next = node
        node.prev = self


class DoublyLinkedList:
    """Creates doubly linked list with sentinel"""

    def __init__(self, *nodes_data):
        """Doubly linked list constructor"""
        self.sen = Node(None)
        self.sen.put_next(self.sen)
        self.__length = 0

        if nodes_data is not None:
            for node in nodes_data:
                self.insert_last(Node(node))

    def __str__(self):
        """String representation"""
        node = self.sen.next
        nodes = []
        if node.data is None:
            return "List is empty"

        while node.data is not None:
            nodes.append(str(node.data))
            node = node.next
        return " <-> ".join(nodes)

    def __iter__(self):
        """How to traverse through the list"""
        node = self.sen.next
        while node.data is not None:
            yield node
            node = node.next

    def __len__(self):
        """Returns __length of the list"""
        return self.__length

    def __getitem__(self, index):
        """How to get the node by its index"""
        if index not in range(0, self.__length):
            raise IndexError
        node = self.sen.next
        for _ in range(index):
            node = node.next
        return node

    def __eq__(self, other):
        return str(self) == str(other)

    def remove_last(self):
        """Removes last node"""
        self.sen.prev.prev.put_next(self.sen)
        self.__length -= 1
        return

    def remove_index(self, index):
        pass

    def remove(self, node_to_remove):
        """Removes first node with matching data starting from the beginning"""
        for node in self:
            if node.data == node_to_remove:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.__length -= 1
                return

    def insert(self, *nodes_data):
        """Puts given node(-s) in the beginning of the list"""
        for each in nodes_data[::-1]:
            node = Node(each)

            node.put_next(self.sen.next)
            self.sen.put_next(node)

            self.sen.next = node
            self.__length += 1
        return

    def insert_last(self, *node_data):
        """Puts given node(-s) in the end of the list"""
        for each in node_data:
            node = Node(each)

            self.sen.prev.put_next(node)
            node.put_next(self.sen)

            self.__length += 1
        return

    def insert_after(self, *node_data, after):
        """Puts given node(-s) after the node in the arguments"""
        pass

    def insert_before(self, *node_data, before):
        """Puts given node(-s) before the node in the arguments"""
        pass

    def head(self):
        """Returns first node"""
        return self.sen.next


class LinkedList:
    """Creates single linked list"""

    def __init__(self, *nodes_data):
        """Linked list constructor"""
        self.head = None
        self.__length = 0
        self.last = self.head
        if nodes_data is not None:
            for node in nodes_data:
                self.put_last(node)

    def __str__(self):
        """String representation"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """How to traverse through the list"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        """Returns __length of the list"""
        return self.__length

    def __getitem__(self, index):
        """How to get the node by its index"""
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def __eq__(self, other):
        return str(self) == str(other)

    def put(self, *node_data):
        """Puts given node(-s) in the beginning of the list"""
        if self.last is None:
            self.last = self.head = Node(node_data[0])
            self.__length += 1

            for each in node_data[1::]:
                node = Node(each)
                self.last.next = node
                self.last = node
                self.__length += 1
            return

        for each in node_data[::-1]:
            node = Node(each)
            node.next = self.head
            self.head = node
            self.__length += 1
        return

    def put_last(self, *node_data):
        """Puts given node(-s) in the end of the list"""
        if self.last is None:
            self.last = self.head = Node(node_data[0])
            self.__length += 1

            for each in node_data[1::]:
                node = Node(each)
                self.last.next = node
                self.last = node
                self.__length += 1
            return

        for each in node_data:
            node = Node(each)
            self.last.next = node
            self.last = node
            self.__length += 1
        return

    def rem(self, node_to_remove):
        """Removes first node with matching data starting from the beginning"""
        if self.head is None:
            return "List is empty"

        elif self.head.data == node_to_remove:
            self.head = self.head.next
            self.__length -= 1
            return

        prev_node = self.head
        for node in self:
            if node.data == node_to_remove:
                prev_node.next = node.next
                self.__length -= 1
                return
            prev_node = node

    def rem_first(self):
        """Removes first node"""
        if self.head is None:
            return "List is empty"
        else:
            res = self.head
            self.head = self.head.next
            self.__length -= 1
            return res


class Queue(DoublyLinkedList):
    """Creates queue. First in - first out"""

    def __str__(self):
        """String representation"""
        node = self.sen.next
        nodes = []
        if node.data is None:
            return "Queue is empty"

        while node.data is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def dequeue(self):
        """Gets item from the head of queue"""
        if self.sen.next is None:
            raise Exception("Queue is empty")
        else:
            res = self.sen.prev
            self.sen.prev.prev.put_next(self.sen)
            return res

    def enqueue(self, *elements):
        """Puts item in the end of queue"""
        for each in elements:
            self.insert(each)


class Stack(LinkedList):
    """Creates stack. Last in - first out"""

    def __str__(self):
        """String representation"""
        if self.head is None:
            return "Stack is empty"

        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def pop(self):
        """Get the last item to enter the stack (LIFO)"""
        if self.head is None:
            raise Exception("Stack is empty")
        else:
            return self.rem_first()

    def push(self, element):
        """Puts item into the stack"""
        self.put(element)

    def top(self):
        return self.head


if __name__ == "__main__":
    # testing doubly linked list

    print("_____________________DOUBLY LINKED LIST______________________")

    doubly_linked = DoublyLinkedList()
    print(f"list: {doubly_linked}")

    doubly_linked.insert(1, 2, 3, 4, 5, 6)
    print(f"after insert: {doubly_linked}")

    doubly_linked.insert(9)
    print(f"after insert: {doubly_linked}")

    doubly_linked.remove_last()
    print(f"last is removed: {doubly_linked}")

    doubly_linked.remove(3)
    print(f"3 is removed: {doubly_linked}")

    doubly_linked.insert_last(0)
    print(f"after insert last: {doubly_linked}")

    print(doubly_linked[0])

    print(f"{doubly_linked.sen.prev} <-> sen <-> {doubly_linked.sen.next}")

    # Testing linked list

    print("________________________LINKED LIST_________________________")

    linked = LinkedList()

    linked.put(1, 2, 3)
    print(linked)

    linked.put('first')
    print(linked)

    linked.put_last(0, 5, 6)
    print(linked)

    linked.rem('first')
    print(linked)

    print(len(linked))

    # Testing queue

    print("____________________________QUEUE____________________________")

    myqueue = Queue()
    myqueue.enqueue(5)
    myqueue.enqueue(66)
    myqueue.enqueue('f')
    myqueue.enqueue(1)
    print(f"queue {myqueue}")
    print(f"dequeue {myqueue.dequeue()}")
    print(f"queue {myqueue}")

    # Testing stack

    print("____________________________STACK____________________________")

    mystack = Stack()
    mystack.push(5)
    mystack.push(66)
    mystack.push('f')
    mystack.push(1)

    print(f"stack {mystack}")
    print(f"top {mystack.top().data}")
    print(f"pop {mystack.pop}")
    print(f"top {mystack.top()}")
    print(f"stack {mystack}")
