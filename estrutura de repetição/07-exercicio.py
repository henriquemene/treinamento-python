from socket import NI_NUMERICHOST


print("-------exercicio 7-------")
nu1=float(input("escolha um numero ? "))
nu2=float(input("escolha um numero ? "))
nu3=float(input("escolha um numero ? "))
nu4=float(input("escolha um numero ? "))
nu5=float(input("escolha um numero ? "))
while True:
    if nu1>nu2 and nu1>nu3 and nu1>nu4 and nu1>nu5:
        print(f"o numero {nu1} é o maior dentre os numeros escolhidos")
        break
    if nu2>nu1 and nu2>nu3 and nu2>nu4 and nu2>nu5:
        print(f"o numero {nu2} é o maior dentre os numeros escolhidos")
        break
    if nu3>nu1 and nu3>nu2 and nu3>nu4 and nu3>nu5:
        print(f"o numero {nu3} é o maior dentre os numeros escolhidos")
        break
    if nu4>nu1 and nu4>nu2 and nu4>nu3 and nu4>nu5:
        print(f"o numero {nu4} é o maior dentre os numeros escolhidos")
        break
    if nu5>nu1 and nu5>nu2 and nu5>nu3 and nu5>nu4:
        print(f"o numero {nu1} é o maior dentre os numeros escolhidos")
        break
