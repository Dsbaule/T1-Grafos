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

	def adjacentes(self, vertice):
		return vertice.adjacentes()

	def grau(self, vertice):
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

	def __str__(self):
		return self.rotulo

	def __repr__(self):
		return self.__str__()

def main():
	g = Grafo()
	# primeira fase
	v1 = Vertice("INE5402")
	v2 = Vertice("MTM5161")
	v3 = Vertice("INE5403")
	v4 = Vertice("EEL5105")
	v5 = Vertice("INE5401")
	# segunda fase
	v6 = Vertice("INE5404")
	v7 = Vertice("MTM7174")
	v8 = Vertice("INE5405")
	v9 = Vertice("MTM5512")
	v10 = Vertice("INE5406")
	v11 = Vertice("INE5407")
	# terceira fase
	v12 = Vertice("INE5408")
	v13 = Vertice("INE5410")
	v14 = Vertice("INE5409")
	v15 = Vertice("MTM5245")
	v16 = Vertice("INE5411")
	# quarta fase
	v17 = Vertice("INE5417")
	v18 = Vertice("INE5413")
	v19 = Vertice("INE5415")
	v20 = Vertice("INE5416")
	v21 = Vertice("INE5412")
	v22 = Vertice("INE5414")
	# quinta fase
	v23 = Vertice("INE5419")
	v24 = Vertice("INE5423")
	v25 = Vertice("INE5420")
	v26 = Vertice("INE5421")
	v27 = Vertice("INE5418")
	v28 = Vertice("INE5422")
	# sexta fase
	v29 = Vertice("INE5427")
	v30 = Vertice("INE5453")
	v31 = Vertice("INE5425")
	v32 = Vertice("INE5430")
	v33 = Vertice("INE5426")
	v34 = Vertice("INE5424")
	# setima fase
	v35 = Vertice("INE5433")
	v36 = Vertice("INE5432")
	v37 = Vertice("INE5429")
	v38 = Vertice("INE5431")
	v39 = Vertice("INE5428")
	# oitava fase
	v40 = Vertice("INE5434")

	g.add_vertice(v1)
	g.add_vertice(v2)
	g.add_vertice(v3)
	g.add_vertice(v4)
	g.add_vertice(v5)
	g.add_vertice(v6)
	g.add_vertice(v7)
	g.add_vertice(v8)
	g.add_vertice(v9)
	g.add_vertice(v10)
	g.add_vertice(v11)
	g.add_vertice(v12)
	g.add_vertice(v13)
	g.add_vertice(v14)
	g.add_vertice(v15)
	g.add_vertice(v16)
	g.add_vertice(v17)
	g.add_vertice(v18)
	g.add_vertice(v19)
	g.add_vertice(v20)
	g.add_vertice(v21)
	g.add_vertice(v22)
	g.add_vertice(v23)
	g.add_vertice(v24)
	g.add_vertice(v25)
	g.add_vertice(v26)
	g.add_vertice(v27)
	g.add_vertice(v28)
	g.add_vertice(v29)
	g.add_vertice(v30)
	g.add_vertice(v31)
	g.add_vertice(v32)
	g.add_vertice(v33)
	g.add_vertice(v34)
	g.add_vertice(v35)
	g.add_vertice(v36)
	g.add_vertice(v37)
	g.add_vertice(v38)
	g.add_vertice(v39)
	g.add_vertice(v40)

	g.conecta(v1,v6)

	g.conecta(v2,v7)
	g.conecta(v2,v8)

	g.conecta(v3,v37)
	g.conecta(v3,v18)
	g.conecta(v3,v19)

	g.conecta(v4,v10)

	g.conecta(v6,v12)
	g.conecta(v6,v13)
	g.conecta(v6,v22)

	g.conecta(v7,v14)
	g.conecta(v7,v25)

	g.conecta(v8,v31)
	g.conecta(v8,v32)

	g.conecta(v9,v14)
	g.conecta(v9,v15)

	g.conecta(v10,v16)

	g.conecta(v11,v39)

	g.conecta(v12,v17)
	g.conecta(v12,v18)
	g.conecta(v12,v19)
	g.conecta(v12,v20)
	g.conecta(v12,v24)

	g.conecta(v13,v21)

	g.conecta(v15,v25)

	g.conecta(v16,v21)

	g.conecta(v17,v23)

	g.conecta(v18,v32)

	g.conecta(v19,v26)
	g.conecta(v19,v37)

	g.conecta(v20,v32)

	g.conecta(v21,v27)
	g.conecta(v21,v34)

	g.conecta(v22,v27)
	g.conecta(v22,v28)
	g.conecta(v22,v37)
	g.conecta(v22,v38)

	g.conecta(v23,v29)
	g.conecta(v23,v30)

	g.conecta(v24,v36)

	g.conecta(v26,v33)

	g.conecta(v29,v35)

	g.conecta(v30,v35)

	g.conecta(v35,v40)

	g.rem_vertice(v12)

	
if __name__ == "__main__":
	main()