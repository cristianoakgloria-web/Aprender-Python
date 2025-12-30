def dobro(v = 0, f = False):
    if f:
        return moeda(v * 2)
    else:
        return v * 2

def metade(v = 0, f = False):
    if f:
        return moeda(v / 2)
    else:
        return v / 2

def aumentar(v = 0, f = False):
    if f:
        return moeda(v + (v * 0.15))
    else:
        return v + (v * 0.15)

def diminuir(v = 0, f = False):
    if f:
        return moeda(v - (v * 0.10))
    else:
        return v - (v * 0.10)

def moeda(v):
    return f'AOA$ {v:.2f}'

def resumo(v):
    m = metade(v, True)
    m = 28 - len(m)
    print('~' * 40)
    print(' ' * 16, 'RESUMO')
    print( '~' * 40)
    print(f'\n  A metade{"." * m}{metade(v, True)}')

    m = dobro(v, True)
    m = 14 - len(m)
    print(f'  O dobro de {moeda(v)}{"." * m}{dobro(v, True)}')

    m = aumentar(v, True)
    m = 18 - len(m)
    print(f'  Com aumento de 15%{"." * m}{aumentar(v, True)}')

    m = diminuir(v, True)
    m = 14 - len(m)
    print(f'  Com uma redução de 10%{"." * m}{diminuir(v, True)}\n')
    print('~' * 40)