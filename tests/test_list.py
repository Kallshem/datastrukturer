import unittest
from exercises.list import Node, UnorderedList


class NodeTests(unittest.TestCase):
    pass

class UnorderedListTests(unittest.TestCase):
    def setUp(self):
        self.ul = UnorderedList()
    
    def test_init(self):
        self.assertEqual(self.ul.head, None)

    def test_is_empty(self):
        self.assertTrue(self.ul.is_empty())
        self.ul.add("hej")
        self.assertFalse(self.ul.is_empty())

    def test_add(self):
        self.ul.add("hello")
        self.assertTrue(self.ul.head.data == "hello")

    def test_size(self):
        self.ul.add("hello")
        self.ul.add("hej")
        self.assertEqual(self.ul.size(), 2)

    def test_search(self):
        self.ul.add("hello")
        self.ul.add("hej")
        self.assertTrue(self.ul.search("hello"))
        self.assertFalse(self.ul.search("FinnsEj"))

    def test_remove(self):
        self.ul.add("hej")
        self.ul.remove("hej")
        self.assertEqual(self.ul.head, None)
        self.assertRaises(ValueError, self.ul.remove, "NotAdded")
        self.assertRaises(ValueError, self.ul.remove, 1)
        self.ul.add("LA")
        self.ul.add("NY")
        self.ul.remove("LA")
        self.assertEqual(self.ul.head.next, None)
        self.assertEqual(self.ul.head.data, "NY")
        self.ul.add("LA")
        self.ul.add("Seattle")
        self.ul.add("Orlando")
        self.ul.append("Soledad")
        self.assertRaises(ValueError, self.ul.remove, "NotAdded")
        self.ul.remove("Seattle")
        self.assertEqual(self.ul.head.next.next.data, "NY")
        self.ul.remove("Orlando")
        self.assertRaises(ValueError, self.ul.remove, "NotAdded")


    def test_append(self):
        self.ul.append("first")
        self.ul.append("second")
        self.ul.append("last")
        self.assertTrue(self.ul.head.next.next.data, "last")

    def test_insert(self):
        self.ul.insert("first")
        self.assertEqual(self.ul.head.next, None)
        self.assertRaises(ValueError, self.ul.insert, 0, 100)
        self.ul.add("firstadd")
        self.ul.add("secondadd")
        self.ul.insert("in between?",1)
        self.ul.insert("last", 3)
        self.assertEqual(self.ul.head.next.data, "in between?")

    def test_index(self):
        self.ul.add("firstadd")
        self.ul.add("secondadd")
        self.ul.insert("in between?",1)
        self.assertTrue(self.ul.index("in between?"), 1)
        self.assertRaises(ValueError, self.ul.index, "NoneExisting")

    def test_pop(self):
        self.assertRaises(ValueError, self.ul.pop, None)  # Nothing to pop
        self.ul.add(1)
        var = self.ul.pop(0)
        self.ul.add(1)
        var2 = self.ul.pop(0)
        self.assertEqual(1, var)
        self.assertEqual(1, var2)
        self.assertTrue(self.ul.is_empty())
        self.ul.add("hej")
        self.ul.add("hejda")
        self.ul.add("tjena")
        var3 = self.ul.pop(1)
        self.assertEqual("hejda", var3)
        self.assertTrue(self.ul.head.next.data == "hej")
        self.assertRaises(ValueError, self.ul.pop, 100)
        self.ul.pop()
        self.assertEqual(self.ul.head.data, "tjena")
        ins = UnorderedList()
        ins.append("first")
        ins.append("second")
        ins.append("last")
        ins.append("*last")
        ins.pop(3)
        self.assertEqual(ins.head.next.next.data, "last")
        ins.pop()
        self.assertEqual(ins.head.next.data, "second")
        ins.pop(1)
        self.assertEqual(ins.head.data, "first")
        ins.append("yes")
        ins.pop(0)
        self.assertEqual(ins.head.data, "yes")
        self.assertRaises(ValueError, ins.pop, 100)
