print("-------exercicio 5-------")

cont=0
populaçaoA=float(input("escolha o numero de habitantes que deseje para a cidade A ?"))
populaçaoB=float(input("escolha o numero de habitantes que deseje  para cidade B  "))
taxaA=float(input("escolha a taxa de crescimento anual   desejada para cidade A "))
taxaB=float(input("escolha a taxa de crescimento anual   desejada para cidade B "))
while populaçaoA <= populaçaoB:
    populaçaoA=(populaçaoA*taxaA)
    populaçaoB=(populaçaoB*taxaB)
    cont = cont +1
        
print(f"demorou {cont} anos para população A ultrapassase populaçao B")