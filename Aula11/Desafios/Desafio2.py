string = 'Tabuada de '
while True:
    m = 1
    n = int(input('Escreve um número> '))

    if n < 0:
        break
    print(f'{string + str(n):_^50}')
    while m <= 12:
        print(f'{n} x {m} = {n * m}')
        m += 1