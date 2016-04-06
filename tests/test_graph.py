import unittest
from exercises.graph import Node, Graph


class NodeTests(unittest.TestCase):
	def setUp(self):
		self.test = Node("test")
		self.test_neighbor = Node("test_neighbor")
		self.test.add_connection(self.test_neighbor, 100)
#fungerar add_connection klaras test_get_connections
	def test_get_connections(self):
		self.assertIn(self.test_neighbor, self.test.get_connections())

	def test_get_weight(self):
		self.assertTrue(self.test.get_weight(self.test_neighbor) == 100)

class GraphTests(unittest.TestCase):
	def test_add_Node(self):
		self.test = Graph()
		self.test.add_node("lorem")
		self.assertIn("lorem", self.test._nodes)

	def setUp(self):
		self.test = Graph()
		self.test.add_node("lorem")
		self.test.add_node("ipsum")
	
	def test_add_edge(self):
		self.test.add_edge("lorem", "ipsum", 100)
		self.assertTrue(self.test._nodes["lorem"]._connections == {"ipsum": 100})

	def test_get_node(self):
		self.assertEqual(self.test.get_node("lorem"), self.test._nodes["lorem"])

	def test_get_graph_nodes(self):
		for node in self.test._nodes:
			self.assertIn(node, self.test.get_graph_nodes())
