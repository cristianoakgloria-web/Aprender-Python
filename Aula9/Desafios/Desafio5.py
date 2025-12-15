for i in range(1, 3 + 1):
    n = int(input('Escreve um número> '))
    n2 = int(input('Escreve outro número> '))
    print(n + n2 if (n + n2) % 2 == 0 else '')