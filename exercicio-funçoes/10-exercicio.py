import random

def dados_craps():
    dado1 = random.randrange(1,7)
    dado2 = random.randrange(1,7)
    soma_dados=dado1 + dado2
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"A soma dos dados é: {soma_dados}")
    return soma_dados

ganhou_jogo = "Você ganhou, parabéns"
perdeu_jogo = " Craps! Você perdeu!!!Tente de novo"
ganha_ponto = "Ponto"


print("GAME - CRAPS")
while True:
    jogar_dado = input("Rolar dados (s ou n)? ")
    if jogar_dado == 'n' or jogar_dado == 'N':
        break
    else:
        resultado_jogo=dados_craps()
    if resultado_jogo == 7 or resultado_jogo == 11 :
        print(ganhou_jogo)
    elif resultado_jogo == 2 or resultado_jogo == 3 or resultado_jogo == 12:
        print(perdeu_jogo)
    else:
        print(ganha_ponto)
while True:
    resulto_dois=dados_craps()
    if resultado_jogo == resulto_dois:
        print(ganhou_jogo)
        break
    elif resulto_dois == 7:
        print(perdeu_jogo)
        break
    else:
        print("Ainda não foi dessa vez!SEGUE O JOGO!!!!")