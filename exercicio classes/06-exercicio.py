import time

class televisor_eletronico:
    def __init__(self, canal_da_televisao="1", volume_da_televisao="50"):
        self.canal = canal_da_televisao
        self.volume = volume_da_televisao

    
    def canal_televisao (self):
        return self.__canal

   
    def canal_televisao_dois (self, numero_canais):

        if numero_canais.isdigit():
            numeros_controle = int(numero_canais)

            if numeros_controle > 0 and numeros_controle <= 150:
                self.__canal = numeros_controle
            else:
                print("Canal Inválido")

        else:
            print("O canal deve ser apenas números!")

    
    def volume_altofalante(self):
        return self.__volume

    
    def volume_televisao(self, numero):

        if numero.isdigit():
            numero_canais = int(numero)

            if numero_canais >= 0 and numero_canais <= 100:
                self.__volume = numero_canais
            else:
                print("O volume deve ser entre 0 e 100")

        else:
            print("O volume deve ser apenas números!")


    def muda_canal(self):
        numero_canal = input("Mudar para CANAL: ")
        self.canal = numero_canal

    def muda_volume(self):
        numero_canais = input("Mudar para VOLUME: ")
        self.volume = numero_canais

    def __str__(self):
        return (f"CANAL: {self.canal} \nvolume: {self.volume}\n ")

def main():
    televisao_01 = televisor_eletronico()

    while True:
        print(televisao_01)

        print("opções ---------")
        print("1 - mudar canal")
        print("2 - mudar volume")
        print("3 - desligar\n ---------------")
        selecionar_canal = input("Selecionar:")

        if selecionar_canal == "1":
            televisao_01.muda_canal()

        elif selecionar_canal == "2":
            televisao_01.muda_volume()

        elif selecionar_canal == "3":
            print("Desligando ...")
            break

        else:
            print("Selecione uma opção válida!")

        time.sleep(2)

main()