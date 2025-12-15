n1 = int(input('Escreve um número> '))
n2 = int(input('Escreve outro número> '))

if n1 > n2:
    print('O número {:.0f} é maior que {:.0f}.'.format(n1, n2))
elif n1 < n2:
    print('O número {:.0f} é maior que {:.0f}.'.format(n2, n1))
else:
    print('O número {:.0f} e o número {:.0f} são iguais.'.format(n1, n2))