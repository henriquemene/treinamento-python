print("-------exercio 6-------")
numero1=float(input("escolha um numero ? "))
numero2=float(input("escolha mais um nuemro ? "))
numero3=float(input("escolha mais um numero ? "))

if numero1 > numero2 and numero1 > numero3:
    print(f"o numero maior dentre os que voce escolheu é o {numero1}")
if numero2 > numero1 and numero2 >numero3:
    print(f"o numero maior dentre os que voce escolheu é o {numero2}")
if numero3 > numero1 and numero3 > numero2:
    print(f"o numero maior dentre os que voce escolheu é o {numero3}")