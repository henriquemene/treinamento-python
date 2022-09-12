print("-------desafio 16-------")
print("CALCULE A QUANTIDADE DE TINTA EO VALOR A SER GASTO!")
parede=int(input("quantos metros quadrados tem sua parede  ? "))
tinta= parede /3
print(f"voce vai precisar de {tinta} litros para pintar sua parede ")

if parede <54:
   print("voce ira precisar apenas de uma lata!")
else :
    lata=parede/54
    lata_total=lata
    print(f"voce vai precisar de {lata_total} lata no total ")
    
preço_lata=lata_total*80
print(f"voce vai pagar o total de R$ {preço_lata}")