class bombaCombustivel:

    def __init__(self,tipo_combustivel,valor_litro,quantidade_combustivel = 0):
        self.tipo_combustivel=tipo_combustivel
        self.valor_litro=valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self,abastecer_tanque):
        litros_colocados = float(abastecer_tanque)/self.valor_litro
        self.alterar_quantidade_de_combutivel(litros_colocados)
        return litros_colocados
        
    def abastecer_por_litro(self,abastecer_tanque):
        self.alterar_quantidade_de_combutivel(abastecer_tanque)
        pagar_combustivel=abastecer_tanque*self.valor_litro
        return pagar_combustivel
        
    def alterar_valor(self,novo_valor_do_combustivel):
        self.valor_litro = novo_valor_do_combustivel
        
    def alterar_combustivel(self,novo_tipo_do_combustivel):
        self.tipo_combustivel = novo_tipo_do_combustivel
        
    def alterar_quantidade_de_combutivel(self,saida_do_combustivel):
        self.quantidade_combustivel-= saida_do_combustivel


   
print ("\nBomba de Combustivel\n")

bomba_de_combustivel=bombaCombustivel("Diesel",50.40,1000)
print ("\nBomba Combustivel(\"Diesel\",50.40,1000)=",\
bomba_de_combustivel.tipo_combustivel,bomba_de_combustivel.valor_litro,bomba_de_combustivel.quantidade_combustivel)


print ("\nAbastecer Por Litro(20)= R$ ",bomba_de_combustivel.abastecer_por_litro(20))
print ("Bomba1= ", bomba_de_combustivel.tipo_combustivel,bomba_de_combustivel.valor_litro,\
bomba_de_combustivel.quantidade_combustivel)


print ("\nAbastecer Por Valor(150)= Lts ",bomba_de_combustivel.abastecer_por_valor(150))
print ("Bomba1= ", bomba_de_combustivel.tipo_combustivel,\
bomba_de_combustivel.valor_litro,bomba_de_combustivel.quantidade_combustivel)


print ("\nAlterarValor(30.32)= R$ ",bomba_de_combustivel.alterar_valor(30.32))
print ("Bomba1= ", bomba_de_combustivel.tipo_combustivel,bomba_de_combustivel.valor_litro,\
bomba_de_combustivel.quantidade_combustivel)


print ("\nAlterar Combustivel(\"Gasolina\")",bomba_de_combustivel.alterar_combustivel("Gasolina"))
print ("Bomba 01= ", bomba_de_combustivel.tipo_combustivel,bomba_de_combustivel.valor_litro,\
bomba_de_combustivel.quantidade_combustivel)