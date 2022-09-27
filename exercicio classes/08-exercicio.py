class Macaco:
    def __init__(self, nome):
        self.nome_do_macaco = nome
        self.bucho_do_macaco = []

    def alimentos_do_macaco(self, comida_do_macaco): 
        self.bucho_do_macaco.append(comida_do_macaco)

    def ver_bucho(self):
        print(f'O bucho do Macaco {self.nome_do_macaco} possui dentro dele:\n {self.bucho_do_macaco}')

    def digerir_alimento(self):
        comida_permitida = ['banana','pera','manga']
        for i in range(len(self.bucho_do_macaco)):
            if self.bucho_do_macaco[i] in comida_permitida:
                print(f'O item {self.bucho_do_macaco[i]} foi digerido no bucho do Macaco {self.nome_do_macaco}')
            else:
                print(f'O item {self.bucho_do_macaco[i]} não foi digerido no bucho do Macaco {self.nome_do_macaco}, ele o vomitou')


Macaco_rita = Macaco('rita') 
Macaco_marco = Macaco('Marco') 

Macaco_rita.alimentos_do_macaco('abacaxi')
Macaco_rita.alimentos_do_macaco('limão')
Macaco_rita.alimentos_do_macaco('pera')
Macaco_rita.ver_bucho()
Macaco_rita.digerir_alimento()
print('\n')
Macaco_marco.alimentos_do_macaco('banana')
Macaco_marco.alimentos_do_macaco('laranja')
Macaco_marco.alimentos_do_macaco('manga')
Macaco_marco.alimentos_do_macaco(Macaco_rita) 
Macaco_marco.ver_bucho()
Macaco_marco.digerir_alimento()
