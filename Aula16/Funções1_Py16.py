def soma(a, b):
    print(f'{a} + {b} = {a + b}')

n1 = float(input('Escreve um número> '))
n2 = float(input('Escreve mais um número> '))

soma(n1, n2)

# Desempacotamento
def somatotal(*a):
    c = 0
    for b in a:
        c += b
    print(f'Soma de todos números: {c}')

somatotal(12, 32, 3, 89, 1)