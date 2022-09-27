class Retangulo:
    def __init__(self, largura, altura):
        self.largura_do_retangulo = largura
        self.altura_do_retangulo = altura

    def encontrar_centro(self): 
        if self.largura_do_retangulo %2 == 1 and self.altura_do_retangulo %2 == 1:
            largura_centro = (self.largura_do_retangulo /2) + 0.5
            altura_centro = (self.altura_do_retangulo /2) + 0.5
            print(f'\nO centro do retangulo está na posição:\nLargura: {largura_centro}\nAltura: {altura_centro}')
        else:
            print(f'\Impossivel achar o centro pois os valores não são impares')
    
class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir_ponto(self):
        if self.x == 0 or self.y == 0:
            ponto_inicio = Ponto.ponto_partida(self)
            print(f'\nO ponto está na posição inicial:\nLargura: {ponto_inicio[0]}\nAltura: {ponto_inicio[1]}')
        else:
            print(f'\nO ponto está na posição:\nLargura: {self.x}\nAltura: {self.y}')
  
    def ponto_partida(self):
        largura_inicial = 2
        altura_inicial = self.y - 1
        print(f'\nO ponto está na posição inicial:\nLargura: {largura_inicial}\nAltura: {altura_inicial}')
        inicio_ponto = [largura_inicial, altura_inicial]
        return inicio_ponto  

classe_retangulo = Retangulo(7,5)
classe_retangulo.encontrar_centro()

classe_retangulo = Ponto(5,6)
classe_retangulo.imprimir_ponto()
classe_retangulo.ponto_partida()