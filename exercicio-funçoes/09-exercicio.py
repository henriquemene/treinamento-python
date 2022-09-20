def numero_reverso(numero):
    return str(numero[::-1])

numero = str(input('Digite um número: '))
print(f"Reverso: {numero_reverso(numero)}")