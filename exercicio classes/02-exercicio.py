class Square:
    def __init__(self, lado="0"):
        self.lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, valor_area):

        if valor_area.isdigit():
            self.__lado = valor_area
        else:
            print("O valor do lado deve ser apenas em numeros")

    def valor_Lado(self):
        print(f"\nO valor do lado é {self.__lado} cm")

    def mudar_Lado(self):
        novo_Lado = input(f"\nMudar lado de {self.__lado} cm para: ")
        self.lado = novo_Lado

    def calculo_Area(self):
        print(f"\nA área do quadrado é  cm² {float(self.__lado) * float(self.__lado)}")

    def __str__(self):
        return f"O quadrado possui {self.__lado} cm de lado e cm² de area {float(self.__lado) * float(self.__lado)}"


def main():
    quadrado_total = Square()
    valor_lado = input("Insira o valor do lado: ")
    quadrado_total.lado = valor_lado

    print(quadrado_total)

    quadrado_total.mudar_Lado()
    quadrado_total.valor_Lado()
    quadrado_total.calculo_Area()


main()