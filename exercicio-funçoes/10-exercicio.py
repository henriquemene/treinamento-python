import random

def dados_craps():
    dado1=random.randrange(1,7)
    dado2=random.randrange(1,7)
    soma_dados=dado1+dado2
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"A soma dos dados é: {soma_dados}")
    return soma_dados

ganhou="Você ganhou, parabéns"
perdeu=" Craps! Você perdeu!!!Tente de novo"
ponto="Ponto"


print("GAME - CRAPS")
while True:
    jogar=input("Rolar dados (s ou n)? ")
    if jogar=='n' or jogar=='N':
        break
    else:
        resulto=dados_craps()
    if resulto==7 or resulto==11:
        print(ganhou)
    elif resulto==2 or resulto==3 or resulto==12:
        print(perdeu)
    else:
        print(ponto)
while True:
    resulto_dois=dados_craps()
    if resulto==resulto_dois:
        print(ganhou)
        break
    elif resulto_dois==7:
        print(perdeu)
        break
    else:
        print("Ainda não foi dessa vez!SEGUE O JOGO!!!!")