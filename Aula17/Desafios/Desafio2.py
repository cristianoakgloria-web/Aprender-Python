def factorial(a = 1, b = True):
    """
    Função para calcular o factorial de um número
    
    :param a: Número a ser calculado
    :param b: (Opicional) Mostrar ou não a conta
    :return: retorna o resultado
    """
    d = a
    if b:
        print(f'{a}! = ', end='')
        for c in range(a - 1, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
                d = d * c
            else:
                print(f'{c} x ', end='')
                d = d * c
        return d
    else:
        for c in range(a - 1, 1, -1):
            d = d * c
        return f'{a}! = {d}'
show = True
print(factorial(int(input('Escreve um número> ')), show))