from labs.src.linked.linked import LinkedList as ll
from labs.src.linked.linked import DoublyLinkedList as dl
from labs.src.linked.linked import Queue as qu
from labs.src.linked.linked import Stack as st


class LinkedHashMap:
    def __init__(self):
        self.buckets = [dl() for _ in range(10)]
        self.len = len(self.buckets)

    def __str__(self):
        res = []
        for i in range(self.len):
            res.append(f'{i} -> {self.buckets[i]}')
        return '\n'.join(res)

    def hash_func(self, key):
        return key % self.len

    def insert(self, key, value):
        index = self.hash_func(key)
        self.buckets[index].insert_last(value)

class HashTable:
    def __init__(self):
        pass


if __name__ == '__main__':
    mapa = LinkedHashMap()
    mapa.insert(10, 1)
    mapa.insert(10, 2)
    mapa.insert(11, 2)
    mapa.insert(20, 3)
    mapa.insert(21, 4)
    print(mapa)
