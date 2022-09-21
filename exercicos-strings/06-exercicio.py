meses_do_ano = {
    '1': 'janeiro',
    '2': 'fevereiro',
    '3': 'março',
    '4': 'abril',
    '5': 'maio',
    '6': 'junho',
    '7': 'julho',
    '8': 'agosto',
    '9': 'setembro',
    '10': 'outubro', 
    '11': 'novembro',
    '12': 'dezembro'        
        }
valor_dias = str(input("Informe o dia do seu nascimento:"))
valor_mes = str(input("Informe o mes do seu nascimento:"))
valor_anos = str(input("Informe o ano do seu nascimento:"))

print ("Data de Nascimento:",str(valor_dias)+"/"+str(valor_mes)+"/"+str(valor_anos))
print(f"Você nasceu no dia {valor_dias},no mes {meses_do_ano[valor_mes]} de  {valor_anos} ")