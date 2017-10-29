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
		self.g = grafo.Grafo()
		self.v1 = grafo.Vertice("A", 6)
		self.v2 = grafo.Vertice("B", 6)
		self.v3 = grafo.Vertice("C", 6)
		self.v4 = grafo.Vertice("D", 6)
		self.v5 = grafo.Vertice("E", 6)
		self.v6 = grafo.Vertice("F", 4)
		self.v7 = grafo.Vertice("G", 4)
		self.v8 = grafo.Vertice("H", 4)
		self.v9 = grafo.Vertice("I", 4)

		self.g.add_vertice(self.v1)
		self.g.add_vertice(self.v2)
		self.g.add_vertice(self.v3)
		self.g.add_vertice(self.v4)
		self.g.add_vertice(self.v5)
		self.g.add_vertice(self.v6)
		self.g.add_vertice(self.v7)
		self.g.add_vertice(self.v8)
		self.g.add_vertice(self.v9)

		self.g.conecta(self.v1,self.v4)
		self.g.conecta(self.v1,self.v5)
		self.g.conecta(self.v2,self.v5)
		self.g.conecta(self.v3,self.v6)
		self.g.conecta(self.v4,self.v7)
		self.g.conecta(self.v5,self.v8)
		self.g.conecta(self.v6,self.v9)
		self.g.conecta(self.v6,self.v8)

	def tearDown(self):
		pass

	def test_rem_vertice(self):

		self.assertEqual(self.v1.sucessores, set([self.v4,self.v5]))
		self.assertEqual(self.v2.sucessores, set([self.v5]))
		self.assertEqual(self.v8.antecessores, set([self.v5, self.v6]))
		self.g.rem_vertice(self.v5)
		self.assertEqual(self.v1.sucessores, set([self.v4]))
		self.assertEqual(self.v2.sucessores, set())
		self.assertEqual(self.v8.antecessores, set([self.v6]))

	def test_ordenacao_topologica(self):
		self.g.rem_vertice(self.v3)
		self.g.rem_vertice(self.v6)
		self.g.rem_vertice(self.v9)
		self.g.conecta(self.v1,self.v2)
		self.g.conecta(self.v2,self.v4)
		self.g.conecta(self.v8,self.v7)
		self.assertIn(self.g.ordenacao_topologica(),[[self.v1,self.v2,self.v4,self.v5,self.v8,self.v7], [self.v1,self.v2,self.v5,self.v8,self.v4,self.v7],[self.v1,self.v2,self.v5,self.v4,self.v8,self.v7]])

	def test_planejamento(self):
		self.assertEqual(self.g.planejamento(), [set([self.v1, self.v2, self.v3]), set([self.v4, self.v5, self.v6]), set([self.v7, self.v8, self.v9])])
		self.g.desconecta(self.v4, self.v7)
		for v in self.g.vertices:
			v.cursada = False

		self.assertEqual(self.g.planejamento(), [set([self.v1, self.v2, self.v3, self.v7]), set([self.v4, self.v5, self.v6]), set([self.v8, self.v9])])
		for v in self.g.vertices:
			v.cursada = False

		self.g.conecta(self.v4, self.v7)
		self.v6.cursada = True
		self.assertEqual(self.g.planejamento(), [set([self.v1, self.v2, self.v3, self.v9]), set([self.v4, self.v5]), set([self.v7, self.v8])])


if __name__ == "__main__":
	unittest.main()
