# len

print("-------exercicio 3-------")


while True:
    nome=str(input("qual o seu nome ? "))
    qnt_caractere= len(nome)

    if qnt_caractere >3:
        print(f"{nome} voce esta cadastrado com sucesso! ")
        break
    else:
        print("digite no minimo 3 caractere ")


while True:     
    idade=float(input("qual é sua idade ? ")) 
    if idade <150 :
        print(f"sua idade é {idade} cadastrado com sucesso ! ")
        break
    else:
        print("digite no maximo 150 e no minimo 0")
     
while True:
    salario=float(input("qual é o seu salario? "))  
    if salario > 1:
        print(f"seu salario e de {salario} cadastrado com sucesso ! ")
        break   
    else:
        print("digite um valor maior que zero  cadastrado com sucesso ! ")


while True: 
    sexo=str(input("qual é o seu sexo ? M ou F ? "))      
    if sexo == "F" :
     print("voce é feminina")
     break
    if sexo == "M":
        print("voce e masculino ")
        break
    else:
      print("porfavor digite F ou M ")


while True:   
    civil=str(input("qual é o seu estado civil? S,C,V,D?  ")) 
    if civil == "S":
        print("voce é solteiro")
        break
    if civil == "C":
        print("voce é casado")
        break
    if civil == "V":
        print("voce é viuva")
        break
    if civil == "D":
        print("voce é divorciada ")
        break
    else:
        print("invalido digite um desses S,C,V,D")
    