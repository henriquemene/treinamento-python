nome_escolhido = input("digite um nome : ").strip()

for caractere in range(len(nome_escolhido)):
    for coluna in range(caractere):
        print(nome_escolhido[coluna],end=" ")
    print()




