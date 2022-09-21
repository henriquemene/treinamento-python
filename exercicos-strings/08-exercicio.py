conjunto_de_caractere = input("Escreva um conjunto de caractere : ").upper().replace(" ", "")

caractere_reverso = conjunto_de_caractere[::-1]

if conjunto_de_caractere == caractere_reverso:
    print(f"É palíndromo, pois, {conjunto_de_caractere} --> {caractere_reverso}" )
else:
    print("Não é palíndromo ")