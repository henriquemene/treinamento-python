print("-------desafio 15-------")
ganho_hora=int(input("quanto voce ganha por hora ?R$ "))
horas_mes=int(input("quantas horas voce trabalha no mes ? "))
bruto= ganho_hora * horas_mes
ir= (bruto *11)/100
inss= (bruto *8)/100
sindicato= (bruto *5)/100
salario_corrigido= (bruto *24)/100
salario_liquido=bruto-salario_corrigido
print(f"ganho bruto {bruto} ")
print(f"- 11% ir  R$ {ir} ")
print(f"- 8% inss R$ {inss}")
print(f" - 5% sindicato R$ {sindicato}")
print(f"salario liquido R$ {salario_liquido}")