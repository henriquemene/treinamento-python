class Ball:
    def __init__(self, color_area="unknown", circunferencia_area=0, material_utilizado="unknown"):
        self.color = color_area
        self.circunf = circunferencia_area
        self.material = material_utilizado

    def troca_Cor(self):
        trocar_cores = input(f"Deseja mudar a cor atual {self.color}? [s/n]")

        trocar_cores = trocar_cores[0].lower()

        if trocar_cores == "s":
            nova_cor = input("\n> Nova Cor: ")
            self.color = nova_cor
        else:
            print(f"Ok a cor continua {self.color}")

    def mostra_Cor(self):
        print(f"\nA cor atual é {self.color}")


def main():
    funcao_bola = Ball("azul", 5, "metal")

    while True:
        funcao_bola.mostra_Cor()
        funcao_bola.troca_Cor()

        continuar_jogo = input("Continuar? [s/n]")
        continuar_jogo = continuar_jogo[0].lower()
        if continuar_jogo == "n":
            break

    funcao_bola.mostraCor()


main()