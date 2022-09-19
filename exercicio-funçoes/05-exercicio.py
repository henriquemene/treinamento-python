def soma_imposto(taxa_imposto, custo):
    return (1 + taxa_imposto/100)*custo


taxa = float(input('Digite a taxa de imposto: '))
custo = float(input('Digite o custo: '))
print('Valor com imposto:', soma_imposto(taxa,custo))