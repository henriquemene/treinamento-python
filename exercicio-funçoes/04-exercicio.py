


def argumento(n):
    if n > 0:
        return "P"
    elif n == 0:
       return "N"
    else:
       return "N"
    

print("POSITIVO OU NEGATIVO?")

n=int(input("digite um numero ? "))
print(f"este numero é  {argumento(n)}")