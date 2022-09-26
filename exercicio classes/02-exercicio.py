class Square:
    def __init__(self, lado="0"):
        self.lado = lado


    def valor_lado(self):
        print(f"\nO valor do lado é {self.lado} cm")

    def mudar_lado(self):
        novo_Lado = input(f"\nMudar lado de {self.lado} cm para: ")
        self.lado = novo_Lado

    def calculo_area(self):
        print(f"\nA área do quadrado é  cm² {float(self.lado) * float(self.lado)}")

    def __str__(self):
        return f"O quadrado possui {self.lado} cm de lado e cm² de area {float(self.lado) * float(self.lado)}"


def main():
    quadrado_total = Square()
    valor_lado = input("Insira o valor do lado: ")
    quadrado_total.lado = valor_lado

    print(quadrado_total)

    quadrado_total.mudar_lado()
    quadrado_total.valor_lado()
    quadrado_total.calculo_area()


main()