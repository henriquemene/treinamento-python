frase_escolhida = input("escolha uma frase: ")

conte_espacos = 0
conte_vogais = 0

for c in range(0,len(frase_escolhida)):
    if frase_escolhida[c] == " ":
        conte_espacos +=  1
    elif frase_escolhida[c] == "a":
        conte_vogais += 1
    elif frase_escolhida[c] == "e":
        conte_vogais += 1
    elif frase_escolhida[c] == "i":
        conte_vogais += 1
    elif frase_escolhida[c] == "o":
        conte_vogais += 1
    elif frase_escolhida[c] == "u":
        conte_vogais += 1



print(f"existe {conte_espacos} espaços em branco em sua frase!" )
print(f"existe {conte_vogais} vogais em sua frase !" )


