hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))

def converter_hora(A):
    return (A -12)

def imprime_hora(A,P):
    if(A <= 12):
        print(A,P,"AM")
    else:
        print(converter_hora(A), P, "PM")

imprime_hora(hora, minuto)