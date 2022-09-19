def valorPagamento(pagamento, dias):
    return pagamento*1.03 + 0.01*dias

quantidade = total = 0

while True:
    pagamento = float(input('Valor da prestação: '))
    if pagamento == 0:
        print(f'Total: {total}. Quantidade: {quantidade} ')
        break
    dias = int(input('Dia em atraso: '))
    print(f'Valor a ser pago: {valorPagamento(pagamento, dias) :.2f}')
    quantidade += 1
    total += valorPagamento(pagamento, dias)
    