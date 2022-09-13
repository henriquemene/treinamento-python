print("-------exercicio 2-------")
nome=str(input("nome de usuario ? "))
senha=str(input("senha ? "))

if senha == nome :
    for c in range(5):
        print("nao aceitamos usuario e senha igual ! ")
        nome=str(input("nome de usuario ? "))
        senha=str(input("senha ? "))
else:
    print("login feito com sucesso !")
    
    