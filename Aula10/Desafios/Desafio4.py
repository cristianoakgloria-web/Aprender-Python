n = int(input('Escreve um número> '))
cont = n - 1
m = n

while cont > 1:
    n = n * cont
    cont -= 1
    print(cont)

print('O factorial de {} é {}.'.format(m, n))