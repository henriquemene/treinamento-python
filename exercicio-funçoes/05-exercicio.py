def soma_imposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo


taxa = float(input('Digite a taxa de imposto: '))
custo = float(input('Digite o custo: '))
print('Valor com imposto:', soma_imposto(taxa,custo))