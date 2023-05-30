import unittest
from labs.src.linked import linked as mc
from labs.src.sorting_methods import sort
import numpy as np
from labs.src.tasks import brackets_labyrinth as bl


class TestLinked(unittest.TestCase):
    def setUp(self) -> None:
        self.doubly_linked = mc.DoublyLinkedList()
        self.linked = mc.LinkedList()
        self.queue = mc.Queue()
        self.stack = mc.Stack()

    def test_DoublyLinkedList(self):
        self.doubly_linked.insert(1, 2, 3, 4, 5, 6)
        self.assertEqual(self.doubly_linked, '1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6')

        self.doubly_linked.insert(9)
        self.assertEqual(self.doubly_linked, '9 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6')

        self.doubly_linked.remove_last()
        self.assertEqual(self.doubly_linked, '9 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5')

        self.doubly_linked.remove(3)
        self.assertEqual(self.doubly_linked, '9 <-> 1 <-> 2 <-> 4 <-> 5')

        self.doubly_linked.insert_last(0)
        self.assertEqual(self.doubly_linked, '9 <-> 1 <-> 2 <-> 4 <-> 5 <-> 0')

    def test_LinkedList(self):
        self.linked.put(1, 2, 3)
        self.assertEqual(self.linked, '1 -> 2 -> 3 -> None')

        self.linked.put('first')
        self.assertEqual(self.linked, 'first -> 1 -> 2 -> 3 -> None')

        self.linked.put_last(0, 5, 6)
        self.assertEqual(self.linked, 'first -> 1 -> 2 -> 3 -> 0 -> 5 -> 6 -> None')

        self.linked.rem('first')
        self.assertEqual(self.linked, '1 -> 2 -> 3 -> 0 -> 5 -> 6 -> None')

        self.linked.rem_first()
        self.assertEqual(self.linked, '2 -> 3 -> 0 -> 5 -> 6 -> None')

        self.assertEqual(len(self.linked), 5)

    def test_Queue(self):
        self.queue.enqueue(5)
        self.assertEqual(self.queue, '5')

        self.queue.enqueue(66)
        self.assertEqual(self.queue, '66 -> 5')

        self.queue.enqueue('f')
        self.assertEqual(self.queue, 'f -> 66 -> 5')

        self.queue.enqueue(1)
        self.assertEqual(self.queue, '1 -> f -> 66 -> 5')

        self.assertEqual(self.queue.dequeue(), 5)

        self.assertEqual(self.queue, '1 -> f -> 66')

    def test_Stack(self):
        self.stack.push(5)
        self.assertEqual(self.stack, '5')

        self.stack.push(66)
        self.assertEqual(self.stack, '66 -> 5')

        self.stack.push('f')
        self.assertEqual(self.stack, 'f -> 66 -> 5')

        self.stack.push(1)
        self.assertEqual(self.stack, '1 -> f -> 66 -> 5')

        self.assertEqual(self.stack.top(), 1)

        self.assertEqual(self.stack.pop(), 1)

        self.assertEqual(self.stack.top(), 'f')

        self.assertEqual(self.stack, 'f -> 66 -> 5')


class TestSort(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = [0.6180755571041122, 0.8442192068307457,
                    0.6114453925936286, 0.6689738637938023,
                    0.8329904617014616, 0.5577943019699589,
                    0.6537321803246283, 0.459733566300109,
                    0.3071402479295656, 0.21801193509708405]

    def test_bubble(self):
        self.assertEqual(sort.bubble(self.arr), [0.21801193509708405, 0.3071402479295656,
                                                 0.459733566300109, 0.5577943019699589,
                                                 0.6114453925936286, 0.6180755571041122,
                                                 0.6537321803246283, 0.6689738637938023,
                                                 0.8329904617014616, 0.8442192068307457])

    def test_insertion(self):
        self.assertEqual(sort.insertion(self.arr), [0.21801193509708405, 0.3071402479295656,
                                                    0.459733566300109, 0.5577943019699589,
                                                    0.6114453925936286, 0.6180755571041122,
                                                    0.6537321803246283, 0.6689738637938023,
                                                    0.8329904617014616, 0.8442192068307457])

    def test_selection(self):
        self.assertEqual(sort.selection(self.arr), [0.21801193509708405, 0.3071402479295656,
                                                    0.459733566300109, 0.5577943019699589,
                                                    0.6114453925936286, 0.6180755571041122,
                                                    0.6537321803246283, 0.6689738637938023,
                                                    0.8329904617014616, 0.8442192068307457])

    def test_merge(self):
        self.assertEqual(sort.merge(self.arr), [0.21801193509708405, 0.3071402479295656,
                                                0.459733566300109, 0.5577943019699589,
                                                0.6114453925936286, 0.6180755571041122,
                                                0.6537321803246283, 0.6689738637938023,
                                                0.8329904617014616, 0.8442192068307457])

    def test_heap(self):
        self.assertEqual(sort.heap(self.arr), [0.21801193509708405, 0.3071402479295656,
                                               0.459733566300109, 0.5577943019699589,
                                               0.6114453925936286, 0.6180755571041122,
                                               0.6537321803246283, 0.6689738637938023,
                                               0.8329904617014616, 0.8442192068307457])

    def test_quick(self):
        self.assertEqual(sort.quick(self.arr), [0.21801193509708405, 0.3071402479295656,
                                                0.459733566300109, 0.5577943019699589,
                                                0.6114453925936286, 0.6180755571041122,
                                                0.6537321803246283, 0.6689738637938023,
                                                0.8329904617014616, 0.8442192068307457])


class TestLabyrinth(unittest.TestCase):
    def setUp(self) -> None:
        self.lab_empty = np.array([])
        self.lab_norm = np.array([[1, 1, 1, 1, 0, 1],
                                  [1, 0, 0, 0, 0, 1],
                                  [1, 1, 0, 1, 0, 1],
                                  [1, 0, 0, 1, 1, 1],
                                  [1, 1, 0, 1, 1, 1]])
        self.lab_all_walls = np.array([[1, 1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1],
                                       [1, 1, 1, 1, 1, 1]])

    def test_path(self):
        self.assertEqual(bl.path(self.lab_empty,
                                 'my start is 2 line and 4',
                                 'finish is 1 1',
                                 'i go d d DOWN left R'), 'Are you even in labyrinth?')

        self.assertEqual(bl.path(self.lab_all_walls,
                                 'my start is 2 line and 4',
                                 'finish is 1 1',
                                 'i go d d DOWN left R'), 'Are you a victim of Philadelphia experiment?')

        self.assertEqual(bl.path(self.lab_norm,
                                 'start is 0 and 4 random numbers 3425 2352',
                                 'fin is 4, 2',
                                 'my way goes DOWN left l D d d'), 'You found the exit')

        self.assertEqual(bl.path(self.lab_norm,
                                 'start is 0 and 4 random numbers 3425 2352',
                                 'fin is 4 2',
                                 'my way goes DOWN left l D RIGHT'), 'You are going the wrong way')


if __name__ == '__main__':
    unittest.main()
