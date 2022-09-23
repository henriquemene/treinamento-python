
arquivo_usuarios = open("./arquivo2.txt", "r")

linhas_do_arquivo = arquivo_usuarios.readlines()


arquivo_usuarios.close()

usuarios_do_arquivo = []
espacos_vazios = []
total_soma = 0
for linha in linhas_do_arquivo:   
    lista_caractere = linha.replace("\n", "").strip().split(" ")
    print(lista_caractere)
    usuarios_do_arquivo.append(lista_caractere[0])
    espacos_vazios.append(int(lista_caractere[-1]))
    print(lista_caractere)
total_soma = int(sum(espacos_vazios))


arquivo_Relatorio = open('./arquivo3.txt', 'w')
arquivo_Relatorio.write(
    'ACME Inc.               Uso do espaco em disco pelos usuarios\n')
arquivo_Relatorio.write(
    '------------------------------------------------------------------------')
arquivo_Relatorio.write('\nNr.  Usuario        Espaco utilizado     %% do uso')


for i in range(0, len(usuarios_do_arquivo)):
    espaco_mega = espacos_vazios[i] / (1024.0 * 1024.0)
    percentua_de_lUso = espacos_vazios[i] / total_soma
    arquivo_Relatorio.write('\n%d - %s   -    %.2f MB    -     %.2f%%' %
        (i + 1, usuarios_do_arquivo[i], espaco_mega, percentua_de_lUso * 100.0))

arquivo_Relatorio.write('\nEspaco total ocupado: %.2f MB' %
    (total_soma / (1024.0 * 1024.0)))
arquivo_Relatorio.write('\nEspaco medio ocupado: %.2f MB' %
    (total_soma / len(usuarios_do_arquivo) / (1024.0 * 1024.0)))

arquivo_Relatorio.close()