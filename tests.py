import unittest
import grafo

class testVertice(unittest.TestCase):

	def setUp(self):
		self.v1 = grafo.Vertice("A")
		self.v2 = grafo.Vertice("B")
		self.v3 = grafo.Vertice("C")
		self.v4 = grafo.Vertice("D")
		self.v5 = grafo.Vertice("E")


	def tearDown(self):
		pass

	def test_grau(self):
		self.v3.adiciona_antecessor(self.v1)
		self.v3.adiciona_antecessor(self.v2)
		self.v3.adiciona_sucessor(self.v4)
		self.v3.adiciona_sucessor(self.v5)

		self.assertEqual(self.v3.grau(), 4)
		self.assertEqual(self.v1.grau(), 0)

		self.v1.adiciona_sucessor(self.v1)
		self.v3.remove_antecessor(self.v2)
		self.v3.remove_sucessor(self.v5)

		self.assertEqual(self.v1.grau(), 1)
		self.assertEqual(self.v3.grau(), 2)

	def test_pode_ser_cursada(self):
		self.assertTrue(self.v1.pode_ser_cursada())
		self.assertTrue(self.v2.pode_ser_cursada())
		self.assertTrue(self.v3.pode_ser_cursada())
		self.assertTrue(self.v4.pode_ser_cursada())
		self.assertTrue(self.v5.pode_ser_cursada())

		self.v3.adiciona_antecessor(self.v1)
		self.v3.adiciona_antecessor(self.v2)
		self.assertFalse(self.v3.pode_ser_cursada())

		self.v1.cursada = True
		self.assertFalse(self.v3.pode_ser_cursada())

		self.v2.cursada = True
		self.assertTrue(self.v3.pode_ser_cursada())

class testGrafo(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	


if __name__ == "__main__":
	unittest.main()
