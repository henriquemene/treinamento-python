
print("------- exercicio 10 -------")
elemento_a=[]
elemento_b=[]
elemento_c=[]
for c in range(10):
    elemento_a.append(input(f"digite o elemento da {c +1}+ posicao do primeiro vetor "))

for c in range(10):
    elemento_b.append(input(f"digite o elemento da {c +1}+ posicao do segundo vetor ")) 

for i in range(10):
    elemento_c.append(elemento_a[i])
    elemento_c.append(elemento_b[i])

print(elemento_c)