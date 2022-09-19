def argumento(n):
    if n > 0:
        print("POSITIVO")
    elif n == 0:
        print("ZERO")

    else:
        print("NEGATIVO")



print("POSITIVO OU NEGATIVO?")

n=int(input("digite um numero ? "))
print("este numero é ", end=' ')
argumento(n)