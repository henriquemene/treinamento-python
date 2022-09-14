while True:
    print("-------exercicio 1-------")
    nota=float(input("escolha uma nota entre 0 e 10 "))
    
    if nota >= 0 and nota <= 10:
        print(f"sua nota foi {nota} ! ")
        break
    else:
        print("nota invalida ")