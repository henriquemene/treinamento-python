print("-------desafio 14-------")
quilos=int(input("quantos quilos de peixe voce trouxe hoje ?"))
multa = quilos - 50 
multa_pagar = multa*4

if quilos < 51:
   print(f"parabens voce não excedeu o limite de peso diario !")
else :
   print(f"voce chegou com o peso de {quilos} e excedeu o limite diario !")
   print(f"voce pagara uma multa de R${multa_pagar}")
