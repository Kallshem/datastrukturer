import unittest
from exercises.tree import BinarySearchTree


class TreeNodeTests(unittest.TestCase):
    def test_init(self):
        pass

class TreeTests(unittest.TestCase):
    def setUp(self):
        self.ul = BinarySearchTree(100)
        self.ul.ints = [150, 50, 140, 40, 145, 160, 155, 157, 153, 55, 49, 51, 39, 41]
        for i in self.ul.ints:
            self.ul.insert(i)

    def test_traverse(self):
        ints = '39, 40, 41, 49, 50, 51, 55, 100, 140, 145, 150, 153, 155, 157, 160'
        self.assertEqual(str(ints), str(self.ul))

    def test_insert(self):
        self.assertTrue(self.ul.left.key == 50)
        self.assertTrue(self.ul.right.key == 150)
        self.assertEqual(self.ul.right.left.key, 140)

    def test_lookup(self):
        self.assertTrue(self.ul.left.right == self.ul.lookup(55))

    def test_delete(self):
        self.ul.delete(50)
        self.ul.ints.remove(50)
        self.assertEqual(str(self.ul.ints), str(self.ul))

#        100
#       /   \
#     98     101
#       \       \
#        99      102