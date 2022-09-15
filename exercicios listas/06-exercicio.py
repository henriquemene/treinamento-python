print("-------exercicio 6 -------")
notaAluno = []
alunoMediaA = 0
for aluno in range(10):
    somaNota=0
    for nota in range(4):
        print(f"digite {nota+1} nota do {aluno + 1}")
        somaNota+= float(input(""))
    notaAluno.append(somaNota/4)   
    if notaAluno[aluno]>= 7.0:
        alunoMediaA +=1

print(f"media dos alunos {notaAluno}")
print(f"numero de alunos em cima da media {alunoMediaA}")
