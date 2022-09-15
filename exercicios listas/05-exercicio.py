print("------- exercicio 5 -------")
valores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

impares = list()
pares = list()
for c in valores:
    if c % 2 != 0:
        impares.append(c)
    else:
        pares.append(c)

print(valores)
print(f'números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
