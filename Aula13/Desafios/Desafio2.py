numeros = []

while True:
    n = int(input('Escreve um número> '))

    if n not in numeros:
        numeros.append(n)

    else:
        print('O número {:.0f} já está lista!'.format(n))
        break

numeros.sort()
print('A lista em ordem crescesnte:', numeros)