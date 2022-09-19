def numero_inteiros(numero):
    return len(str(numero))

numero = int(input('Digite um número: '))
print(f'Esse número tem {numero_inteiros(numero)} dígitos')