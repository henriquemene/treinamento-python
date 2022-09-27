class BichinhoEletronico:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
		self.fome = 100
		self.saude = 100

	def nome_do_bichinho(self):
		return self.nome

	def outro_nome(self, novo_nome):
		self.nome = novo_nome

	def idade_do_bichinho(self):
		return self.idade

	def outra_idade(self, nova_idade):
		self.idade = nova_idade

	def fome_do_bichinho(self):
		return self.fome

	def definir_fome(self, nova_fome_do_bichinho):
		self.fome = nova_fome_do_bichinho

	def saude_do_bichinho(self):
		return self.saude

	def definir_saude(self,nova_saude_do_bichinho):
		self.saude = nova_saude_do_bichinho

	def humor_do_bichinho(self):
		if self.fome_do_bichinho() >= 70 and self.saude_do_bichinho() >= 70:
			return "estou feliz!"

		elif self.fome_do_bichinho() >= 50 and self.saude_do_bichinho() >= 50:
			return "não estou muito bem !"

		elif self.fome_do_bichinho() >= 30 and self.saude_do_bichinho() >= 30:
			return "estou muito bravo!"

		else:
			return "estou tão fraco que não posso responder!"

bichinho = BichinhoEletronico("Bolinha", 2)

print( bichinho.nome_do_bichinho() )
print( bichinho.idade_do_bichinho() )
print( bichinho.humor_do_bichinho() )

bichinho.definir_saude(30)
bichinho.definir_fome(70)

print( bichinho.humor_do_bichinho() )



