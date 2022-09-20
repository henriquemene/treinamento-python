print("------- exercicio 8 -------")
idade_pessoa=[]
altura_pessoa=[]
for c in range(5):
    idade_pessoa.append(input("qual é a sua idade ?"))
    altura_pessoa.append(input("qual é a sua altura ? "))
idade_pessoa=list(reversed(idade_pessoa))
altura_pessoa=list(reversed(altura_pessoa))
print(f"idade {idade_pessoa}")
print(f"altura {altura_pessoa}")
