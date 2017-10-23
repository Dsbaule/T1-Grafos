import random

class Grafo():
	
	def __init__(self):
		self.vertices = set()

	def add_vertice(self, vertice):
		self.vertices.add(vertice)

	def conecta(self, v1, v2):
		v1.adiciona_sucessor(v2)
		v2.adiciona_antecessor(v1)

	def desconecta(self, v1, v2):
		v1.remove_sucessor(v2)
		v2.remove_antecessor(v1)

	def rem_vertice(self, vertice):
		for antecessor in vertice.antecessores:
			antecessor.remove_sucessor(vertice)
		for sucessor in vertice.sucessores:
			sucessor.remove_antecessor(vertice)

		self.vertices.remove(vertice)

	def ordem(self):
		return len(self.vertices)

	def vertices(self):
		return self.vertices

	def um_vertice(self):
		rv = random.sample(self.vertices, 1)
		return rv[0]

	def adjacentes(vertice):
		return vertice.adjacentes()

	def grau(vertice):
		return vertice.grau()

class Vertice():
	
	def __init__(self, rotulo):
		self.rotulo = rotulo
		self.antecessores = set()
		self.sucessores = set()

	def adiciona_antecessor(self, vertice):
		self.antecessores.add(vertice)

	def adiciona_sucessor(self, vertice):
		self.sucessores.add(vertice)

	def remove_antecessor(self, vertice):
		self.antecessores.remove(vertice)

	def remove_sucessor(self, vertice):
		self.sucessores.remove(vertice)

	def adjacentes(self):
		return self.antecessores | self.sucessores

	def grau(self):
		return len(self.adjacentes())
