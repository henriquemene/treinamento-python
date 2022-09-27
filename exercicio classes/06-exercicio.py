import time

class televisorEletronico:
    def __init__(self, canal_da_televisao="1", volume_da_televisao="50"):
        self.canal = canal_da_televisao
        self.volume = volume_da_televisao

    
    def canais_de_televisao (self):
        return self.__canal

   
    def canais_da_segunda_televisao (self, numero_canais):

        if numero_canais.isdigit():
            numeros_controle = int(numero_canais)

            if numeros_controle > 0 and numeros_controle <= 150:
                self.__canal = numeros_controle
            else:
                print("Canal Inválido")

        else:
            print("O canal deve ser apenas números!")

    
    def volume_da_televisao(self):
        return self.__volume

    
    def segundo_volume_da_televisao(self, numero):

        if numero.isdigit():
            numero_canais = int(numero)

            if numero_canais >= 0 and numero_canais <= 100:
                self.__volume = numero_canais
            else:
                print("O volume deve ser entre 0 e 100")

        else:
            print("O volume deve ser apenas números!")


    def mudar_canal(self):
        numero_canal = input("Mudar para CANAL: ")
        self.canal = numero_canal

    def mudar_volume(self):
        numero_canais = input("Mudar para VOLUME: ")
        self.volume = numero_canais

    def __str__(self):
        return (f"CANAL: {self.canal} \nvolume: {self.volume}\n ")

def main():
    primeira_televisao = televisorEletronico()

    while True:
        print(primeira_televisao)

        print("opções ---------")
        print("1 - mudar canal")
        print("2 - mudar volume")
        print("3 - desligar\n ---------------")
        selecionar_canal = input("Selecionar:")

        if selecionar_canal == "1":
            primeira_televisao.mudar_canal()

        elif selecionar_canal == "2":
            primeira_televisao.mudar_volume()

        elif selecionar_canal == "3":
            print("Desligando ...")
            break

        else:
            print("Selecione uma opção válida!")

        time.sleep(2)

main()