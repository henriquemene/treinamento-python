class Pessoa:
    def __init__(self, nome_usuario: str, idade_usuario: int, peso_usuario: float, altura_usuario: float):
        self.nome = nome_usuario
        self.idade = idade_usuario
        self.peso = peso_usuario
        self.altura = altura_usuario

    def envelhecer_idade(self):
        if self.idade < 21:
            self.altura += 0.5

        self.idade += 1

    def engordar_quilos(self, peso_total):
        self.peso += peso_total

    def emagrecer_quilos(self, peso_total):
        self.peso -= peso_total

    def crescer_altura(self, altura_usuario):
        self.altura += altura_usuario


    def mostra_pessoa(self):
        print(f"Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm")


nome_usuario = Pessoa('henrique', 21, 63, 168)
nome_usuario.mostra_pessoa()
nome_usuario.envelhecer_idade()
nome_usuario.emagrecer_quilos(3)
nome_usuario.mostra_pessoa()