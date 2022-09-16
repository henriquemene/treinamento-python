def criar_e_mostrar_triangulo(quantidade_de_linhas):
    for linha in range(1,quantidade_de_linhas + 1):
        for coluna in range(linha):
            print(linha,end=" ")
        print()
resposta = int(input("digite um numero : "))

print("------- exercicio 10 -------")

criar_e_mostrar_triangulo(resposta)
