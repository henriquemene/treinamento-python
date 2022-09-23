
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


relatorio_do_arquivo = open('./arquivo3.txt', 'w')
relatorio_do_arquivo.write(
    'ACME Inc.               Uso do espaco em disco pelos usuarios\n')
relatorio_do_arquivo.write(
    '------------------------------------------------------------------------')
relatorio_do_arquivo.write('\nNr.  Usuario        Espaco utilizado     %% do uso')


for i in range(0, len(usuarios_do_arquivo)):
    espaco_mega = espacos_vazios[i] / (1024.0 * 1024.0)
    percentua_de_uso = espacos_vazios[i] / total_soma
    relatorio_do_arquivo.write('\n%d - %s   -    %.2f MB    -     %.2f%%' %
        (i + 1, usuarios_do_arquivo[i], espaco_mega, percentua_de_uso * 100.0))

relatorio_do_arquivo.write('\nEspaco total ocupado: %.2f MB' %
    (total_soma / (1024.0 * 1024.0)))
relatorio_do_arquivo.write('\nEspaco medio ocupado: %.2f MB' %
    (total_soma / len(usuarios_do_arquivo) / (1024.0 * 1024.0)))

relatorio_do_arquivo.close()