from labs.src.linked.linked import LinkedList as ll
from labs.src.linked.linked import DoublyLinkedList as dl
from labs.src.linked.linked import Queue as qu
from labs.src.linked.linked import Stack as st


class LinkedHashMap:
    def __init__(self):
        self.buckets = [dl() for _ in range(10)]
        self.len = len(self.buckets)

    def __repr__(self):
        for i in range(self.len):
            print(f'{i} -> {self.buckets[i]}')

    def hash_func(self, key):
        return key % self.len

    def insert(self, key, value):
        index = self.hash_func(key)
        self.buckets[index].insert_last(value)


if __name__ == '__main__':
    mapa = LinkedHashMap()
    mapa.insert(10, 1)
    mapa.insert(11, 2)
    mapa.insert(20, 3)
    mapa.insert(21, 4)
    print(mapa)
