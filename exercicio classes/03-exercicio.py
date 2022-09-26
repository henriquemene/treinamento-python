class Retangulo:
    def __init__(self,comprimento_piso, largura_total):
        self.comprimento = comprimento_piso
        self.largura = largura_total

    def mudar_valor_comprimento(self,novo_comprimento):
        self.comprimento = novo_comprimento

    def mudar_valor_largura(self, nova_largura):
        self.largura = nova_largura

    def retornar_valor_lados(self):
        print(f"{self.comprimento}cm, {self.largura}cm")

    def calcular_area(self):
        area_selecionada = self.largura * self.comprimento
        print(f"{area_selecionada}m quadrados")     
        return area_selecionada                   


    def calcular_perimetro(self):
        perimetro_local = 2*self.largura + 2*self.comprimento
   
        return perimetro_local               


retangulo_area = Retangulo(4,10)

print(retangulo_area.__dict__)
retangulo_area.retornar_valor_lados()
retangulo_area.calcular_area()                  
retangulo_area.calcular_perimetro()             

retangulo_area.mudar_valor_comprimento(3)
retangulo_area.mudar_valor_largura(12)
print(retangulo_area.__dict__)
retangulo_area.retornar_valor_lados()
retangulo_area.calcular_area()                 
retangulo_area.calcular_perimetro()              

comprimento_do_local = float(input("selecione o comprimento do local:" ))
comprimento_do_piso = float(input("selecione a largura do local:" ))

local_escolhido = Retangulo(comprimento_do_local,comprimento_do_piso)

print (f"serão necessários {local_escolhido.calcular_area()}m quadrado(s) de piso e {local_escolhido.calcular_perimetro()}m de rodapés para suprir o local")