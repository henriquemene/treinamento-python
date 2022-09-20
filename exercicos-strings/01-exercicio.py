
primeira_string = str(input ("digite algo  " ))
segunda_string = str(input("digite algo novamente  " ))

primeira_quantidade_string=primeira_string
segunda_quantidade_string=segunda_string


print(f"tamanho de {primeira_string} : {len(primeira_quantidade_string)} caractere " )
print(f"tamanho de {segunda_string}  : {len(segunda_quantidade_string)} caractere " )

if primeira_quantidade_string == segunda_quantidade_string:
    print("as duas strings posuem tamanhos iguais ")
else:
    print("as duas strings tem tamanho diferentes ")

if primeira_string == segunda_string:
    print("as duas strings posuem conteudo iguais ")
else:
    print("as duas strings posuem conteudo diferentes")