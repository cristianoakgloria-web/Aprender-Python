numeros = []
ímpares = []
pares = []

while True:
    n = int(input('Escreve um número> '))

    if n not in numeros:
        numeros.append(n)

    else:
        print('O número {:.0f} já está lista!'.format(n))
        break

for i in numeros:
    if i%2:
        ímpares.append(i)

    else:
        pares.append(i)

print(f'\nLista Original: {numeros}\nLista de Números Pares: {pares}\nLista de Números Ímpares: {ímpares}')