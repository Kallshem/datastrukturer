import unittest
from exercises.simple import Stack, Queue
from exercises.exceptions import EmptyStack, EmptyQueue

class StackTests(unittest.TestCase):
    def test_Stack(self):
        self.assertIn('__init__', dir(Stack))
        self.assertIn('pop', dir(Stack))
        self.assertIn('is_empty', dir(Stack))
        testins = Stack()
        testins.push("first")
        testins.push(2)
        testins.push(3)
        self.assertEqual(testins.data, [3, 2, "first"])
        testins.pop()
        self.assertEqual(testins.data, [2, "first"])
        self.assertEqual(testins.peek(), 2)
        self.assertEqual(testins.size(), 2)
        self.assertEqual(testins.is_empty(), False)
        testins.pop()
        testins.pop()
        self.assertEqual(testins.is_empty(), True)
        self.assertRaises(EmptyStack, testins.pop)
        self.assertRaises(EmptyStack, testins.peek)




class QueueTests(unittest.TestCase):
    def test_Queue(self):
        self.assertIn('__init__', dir(Queue))
        self.assertIn('dequeue', dir(Queue))
        self.assertIn('is_empty', dir(Queue))
        testins = Queue()
        testins.enqueue(1)
        testins.enqueue("two")
        self.assertEqual(testins.queue, [1, "two"])
        testins.dequeue()
        self.assertEqual(testins.queue, ["two"])
        self.assertEqual(testins.is_empty(), False)
        self.assertEqual(testins.size(), 1)
        testins.dequeue()
        self.assertEqual(testins.is_empty(), True)
        self.assertEqual(testins.queue, [])
        self.assertRaises(EmptyQueue, testins.dequeue)
        



#unittest.TestCase: ett objekt skapas?
#kört utan manage.py?