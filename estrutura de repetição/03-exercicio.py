# len

print("-------exercicio 3-------")
nome=str(input("qual o seu nome ? "))
idade=float(input("qual é sua idade ? "))
salario=float(input("qual é o seu salario? "))
sexo=str(input("qual é o seu sexo ? M ou F ? "))
civil=str(input("qual é o seu estado civil? s,c,v,d?  "))

qnt_caractere= len(nome)

if qnt_caractere <3:
    print("digite no minimo 3 caractere ")
else:
    print(f"{nome} voce esta cadastrado com sucesso! ")
    
    
if idade >150 :
    print("digite no maximo 150 e no minimo 0")
else:
    print(f"sua idade é {idade} cadastrado com sucesso ! ")
    
    
if salario < 1:
    print("digite um valor maior que zero ! ")
else:
    print(f"seu salario e de {salario}")
    
if sexo == "F" :
    print("voce é feminina")
if sexo == "M":
    print("voce e masculino ")
else:
    print("porfavor digite F ou M ")
    
    
if civil == "S":
    print("voce é solteiro")
if civil == "C":
    print("voce é casado")
if civil == "V":
    print("voce é viuva")
if civil == "D":
    print("voce é divorciada ")
else:
    print("invalido digite um desses S,C,V,D")
    