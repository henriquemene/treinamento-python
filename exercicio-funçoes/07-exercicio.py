def valor_Pagamento(total_pagamento, total_dias):
    return total_pagamento*1.03 + 0.01*total_dias*total_pagamento

quantidade = total = 0

while True:
    total_pagamento = float(input('Valor da prestação: '))
    if total_pagamento == 0:
        print(f'Total: {total}. Quantidade: {quantidade} ')
        break
    total_dias = int(input('Dia em atraso: '))
    print(f'Valor a ser pago: {valor_Pagamento(total_pagamento, total_dias) :.2f}')
    quantidade += 1
    total += valor_Pagamento(total_pagamento, total_dias)
