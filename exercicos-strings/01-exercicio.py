
primeira_string = str(input ("digite algo  " ))
segunda_string = str(input("digite algo novamente  " ))

tamanho_string_1=len(primeira_string)
tamanho_string_2=len(segunda_string)

print(f"tamanho de {primeira_string} : {tamanho_string_1} caractere " )
print(f"tamanho de {segunda_string}  : {tamanho_string_2} caractere " )

if tamanho_string_1 == tamanho_string_2:
    print("as duas strings posuem tamanhos iguais ")
else:
    print("as duas strings tem tamanho diferentes ")

if primeira_string == segunda_string:
    print("as duas strings posuem conteudo iguais ")
else:
    print("as duas strings posuem conteudo diferentes")