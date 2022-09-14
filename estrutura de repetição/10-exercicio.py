print("-------exercicio 10-------")
numero1=int(input("digite um numero inteiro ? "))
numero2=int(input("digite outro numero inteiro ? "))
if numero1 < numero2:
    for i in range(numero1+1,numero2+1):
        print(i)

a=numero2
b=numero1
for i in range(a+1,b,1):
    print(i)