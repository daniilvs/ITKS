class Node:
    """Creates myqueue node. Node contains information about data which is put in it and
    pointers to the next (for both linked list and doubly linked list) and to the 
    previous (only for doubly linked list) nodes in list"""
    def __init__(self, data):
        """Node constructor"""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """String representation"""
        return str(self.data)

    def put_next(self, node):
        """(only for doubly linked list) puts node from parentheses
        ahead of the self one"""
        self.next = node
        node.prev = self


class DoublyLinkedList:
    """Creates myqueue doubly linked list with sentinel"""
    def __init__(self, *nodes_data):
        """Doubly linked list constructor"""
        self.sen = Node(None)
        self.sen.put_next(self.sen)
        self.length = 0

        if nodes_data is not None:
            for node in nodes_data:
                self.insert_last(Node(node))

    def __repr__(self):
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
        """Returns length of the list"""
        return self.length

    def __getitem__(self, item):
        """How to get the node by its data"""
        for node in self:
            if node.data == item:
                return node

    def remove_last(self):
        """Removes last node"""
        if self.sen.next is None:
            raise Exception("List is empty")
        else:
            self.sen.prev.prev.put_next(self.sen)
            self.length -= 1
            return

    def remove(self, node_to_remove):
        """Removes first node with matching data starting from the beginning"""
        if self.sen.next is None:
            raise Exception("List is empty")
        else:
            for node in self:
                if node.data == node_to_remove:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.length -= 1
                    return

    def insert(self, *node_data):
        """Puts given node(-s) in the beginning of the list"""
        for each in node_data[::-1]:
            node = Node(each)

            node.put_next(self.sen.next)
            self.sen.put_next(node)

            self.sen.next = node
            self.length += 1
        return

    def insert_last(self, *node_data):
        """Puts given node(-s) in the end of the list"""
        for each in node_data:
            node = Node(each)

            self.sen.prev.put_next(node)
            node.put_next(self.sen)

            self.length += 1
        return

    def insert_after(self, node_data, after):
        """Puts given node(-s) after the node in the arguments"""
        pass

    def head(self):
        """Returns first node"""
        return self.sen.next


class LinkedList:
    """Creates myqueue single linked list"""
    def __init__(self, *nodes_data):
        """Linked list constructor"""
        self.head = None
        self.length = 0
        try:
            node = Node(nodes_data[0])
            self.head = node
            self.length += 1
        except IndexError:
            self.head = None
        except AttributeError:
            self.head = None
        else:
            for elem in nodes_data[1:]:
                node.next = Node(elem)
                node = node.next
                self.length += 1

    def __repr__(self):
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
        """Returns length of the list"""
        return self.length

    def __getitem__(self, item):
        """How to get the node by its data"""
        for node in self:
            if node.data == item:
                return node

    def put(self, *node_data):
        """Puts given node(-s) in the beginning of the list"""
        for each in node_data[::-1]:
            node = Node(each)
            node.next = self.head
            self.head = node
            self.length += 1
        return

    def put_last(self, *node_data):
        """Puts given node(-s) in the end of the list"""
        last = None

        if self.head is None:
            last = self.head
        else:
            for current in self:
                if current.next is None:
                    last = current

        for each in node_data:
            node = Node(each)
            last.next = node
            last = node
            self.length += 1
        return

    def put_before(self, new_node_data, before):
        """Puts given node(-s) before the node in the arguments"""
        if self.head is None:
            raise Exception("List is empty")

        elif self.head.data == before:
            self.put(new_node_data)

        prev_node = self.head
        for node in self:
            if node.data == before:
                new_node = Node(new_node_data)
                prev_node.next = new_node
                new_node.next = node
                self.length += 1
                return
            prev_node = node

    def put_after(self, new_node_data, after):
        """Puts given node(-s) after the node in the arguments"""
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == after:
                new_node = Node(new_node_data)
                new_node.next = node.next
                node.next = new_node
                self.length += 1
                return

    def rem(self, node_to_remove):
        """Removes first node with matching data starting from the beginning"""
        if self.head is None:
            raise Exception("List is empty")

        elif self.head.data == node_to_remove:
            self.head = self.head.next
            self.length -= 1
            return

        prev_node = self.head
        for node in self:
            if node.data == node_to_remove:
                prev_node.next = node.next
                self.length -= 1
                return
            prev_node = node


class Queue:
    """Creates myqueue queue. First in - first out"""
    def __init__(self):
        """Queue constructor"""
        self.queue = DoublyLinkedList()
        self.tail = self.queue.head()

    def __repr__(self):
        """String representation"""
        node = self.queue.sen.next
        nodes = []
        if node.data is None:
            return "Queue is empty"

        while node.data is not None:
            nodes.append(str(node.data))
            node = node.next
        return " <-> ".join(nodes)

    def dequeue(self):
        """Gets item from the head of queue"""
        if self.queue.sen.next is None:
            raise Exception("List is empty")
        else:
            res = self.queue.sen.prev
            self.queue.sen.prev.prev.put_next(self.queue.sen)
            return res

    def enqueue(self, *element):
        """Puts item in the end of queue"""
        for each in element:
            self.queue.insert(each)


class Stack:
    """Creates myqueue stack. Last in - first out"""
    def __init__(self):
        """Stack constructor"""
        self.stack = LinkedList()
        self.top = 0

    def __repr__(self):
        """String representation"""
        node = self.stack.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def pop(self):
        """Get the last item to enter the stack (LIFO)"""
        if self.stack.head is None:
            raise Exception("Stack is empty")
        else:
            self.top -= 1
            res = self.stack.head.data
            self.stack.head = self.stack.head.next
            return res

    def push(self, element):
        """Puts item into the stack"""
        self.stack.put(element)
        self.top += 1


if __name__ == "__main__":

    # testing doubly linked list

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

    doubly_linked.insert_last(0, -1, -2, -3, -4)
    print(f"after insert last: {doubly_linked}")

    print(f"{doubly_linked.sen.prev} <-> sen <-> {doubly_linked.sen.next}")

    # Testing linked list

    linked = LinkedList(1, 2, 3)
    print(linked)

    linked.put('first')
    print(linked)

    linked.put_last(0, 5, 6)
    print(linked)

    linked.rem('first')
    print(linked)

    print(len(linked))

    # Testing queue

    myqueue = Queue()
    myqueue.enqueue(5, 6, 5, 4, 6)
    # myqueue.enqueue(66)
    # myqueue.enqueue('f')
    # myqueue.enqueue(1)
    print(f"queue {myqueue}")
    # print(f"head {myqueue.queue.head.data}")
    print(f"dequeue {myqueue.dequeue()}")
    # print(f"tail {myqueue.tail}")
    print(f"queue {myqueue}")

    # Testing stack

    mystack = Stack()
    mystack.push(5)
    mystack.push(66)
    mystack.push('f')
    mystack.push(1)
    print(f"top {mystack.top}")
    print(f"stack {mystack}")
    print(f"head {mystack.stack.head.data}")
    print(f"pop {mystack.pop()}")
    print(f"top {mystack.top}")
    print(f"stack {mystack}")
