import os

def  validar_valido ( ip_string ):
    partes  =  ip_string.split( "." )
    if  len( partes ) !=  4 :
        return  False
    for  c  in  partes :
        if  not  c.isdigit():
            return  False
        parte_interagir  =  int ( c )
        if  parte_interagir  <  0  or  parte_interagir  >  255 :
            return  False
    return  True

if  os.path.exists( "./arquivo.txt"):

    ips_arquivo  =  open( "./arquivo.txt" , "r" )

    lista_ips  =  ips_arquivo.read().split("\n")
    
    ips_validos  = []
    ips_invalidos  = []
    
    for  i  in  lista_ips :
        if  validar_valido( i ) ==  True :
            ips_validos.append( i )
        else :
            ips_invalidos.append( i )
    
    if  len( ips_validos ) >  0  or  len( ips_validos ) >  0 :
        arquivo_relatorio  =  open( "resposta.txt" , "wt" )
        
        if  len ( ips_validos ) >  0 :
            arquivo_relatorio.write( "[Endereços válidos:] \n " )
            for  valido  in  ips_validos :
                arquivo_relatorio.write( valido + " \n " )
        
        if  len ( ips_invalidos ) >  0 :
            arquivo_relatorio.write( " \n [Endereços inválidos:] \n " )
            for  invalido  in  ips_invalidos :
                arquivo_relatorio.write( invalido + " \n " )
        
        arquivo_relatorio.close()
