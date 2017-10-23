import random
from time import sleep
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

	def ordenacao_topologica(self):
		s = self.sumidouros()
		l = []

		def visita(vertice):
			if not vertice.visitado:
				vertice.visitado = True
				for v in vertice.antecessores:
					visita(v)
				l.append(vertice)

		for sumidouro in s:
			visita(sumidouro)

		self.limpa_vertices()

		return l

	def planejamento(self):
		pass

	def verifica_disciplinas(self):
		for v in self.vertices:
			if v.cursada == False and v.visitado == False:
				return True
		return False

	def limpa_vertices(self):
		for v in self.vertices:
			v.visitado = False

	def sumidouros(self):
		s = set()
		for v in self.vertices:
			if len(v.sucessores) == 0:
				s.add(v)
		return s

class Vertice():
	
	def __init__(self, rotulo, carga_horaria, cursada=False):
		self.rotulo = rotulo
		self.antecessores = set()
		self.sucessores = set()
		self.visitado = False
		self.carga_horaria = carga_horaria
		self.cursada = cursada

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
	v1 = Vertice("INE5402",6,True)
	v2 = Vertice("MTM5161",4,True)
	v3 = Vertice("INE5403",6,True)
	v4 = Vertice("EEL5105",5,True)
	v5 = Vertice("INE5401",2,True)
	# segunda fase
	v6 = Vertice("INE5404",6,True)
	v7 = Vertice("MTM7174",4,True)
	v8 = Vertice("INE5405",5,True)
	v9 = Vertice("MTM5512",4,True)
	v10 = Vertice("INE5406",5,True)
	v11 = Vertice("INE5407",3,True)
	# terceira fase
	v12 = Vertice("INE5408",6,True)
	v13 = Vertice("INE5410",4,True)
	v14 = Vertice("INE5409",4,True)
	v15 = Vertice("MTM5245",4,True)
	v16 = Vertice("INE5411",6,True)
	# quarta fase
	v17 = Vertice("INE5417",5,True)
	v18 = Vertice("INE5413",4,True)
	v19 = Vertice("INE5415",4,True)
	v20 = Vertice("INE5416",5,True)
	v21 = Vertice("INE5412",4,True)
	v22 = Vertice("INE5414",4,True)
	# quinta fase
	v23 = Vertice("INE5419",4)
	v24 = Vertice("INE5423",4)
	v25 = Vertice("INE5420",4)
	v26 = Vertice("INE5421",4)
	v27 = Vertice("INE5418",4)
	v28 = Vertice("INE5422",4)
	# sexta fase
	v29 = Vertice("INE5427",4)
	v30 = Vertice("INE5453",4)
	v31 = Vertice("INE5425",4)
	v32 = Vertice("INE5430",4)
	v33 = Vertice("INE5426",4)
	v34 = Vertice("INE5424",4)
	# setima fase
	v35 = Vertice("INE5433",6)
	v36 = Vertice("INE5432",4)
	v37 = Vertice("INE5429",4)
	v38 = Vertice("INE5431",4)
	v39 = Vertice("INE5428",4)
	# oitava fase
	v40 = Vertice("INE5434",6)

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

	print(g.ordenacao_topologica())
	
if __name__ == "__main__":
	main()