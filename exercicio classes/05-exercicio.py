class contaCorrente:

    def __init__(self,numero_conta, nome_correntista,saldo_bancario=0):
        self.saldo = saldo_bancario
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposito_bancario(self,valor_deposito):
        self.saldo += valor_deposito
        return self.saldo

    def saque_dinheiro(self,valor_saque):
        self.saldo -= valor_saque
        return self.saldo

saldo_total = contaCorrente(250,"Henrique Menegatti")

print (saldo_total.__dict__)

saldo_total.deposito_bancario(25)
print (saldo_total.__dict__)

saldo_total.saque_dinheiro(10)
print (saldo_total.__dict__)