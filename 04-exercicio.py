print("-------desafio 04-------")
nome_aluno = str(input("digite o nome do aluno "))
primeira_nota =int(input("digite a primeira nota do {} ? ".format(nome_aluno)))
segunda_nota = int(input("digite a segunda nota do {} ?".format(nome_aluno)))
media = (primeira_nota + segunda_nota) /2
print("a media do aluno {} é {}".format(nome_aluno,media))