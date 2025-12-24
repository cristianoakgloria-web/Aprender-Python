def leiaInt(n):
    """
    A função leiaInt serve para gravar valor em uma variável caso sejá um número
    
    :param n: Variavél a ser verificada
    :return: retorna o valor númerico
    """
    if n.isdecimal():
        return n
    
número = leiaInt(input('Escreve um número> '))
print(número)