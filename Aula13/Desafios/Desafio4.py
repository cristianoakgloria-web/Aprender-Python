numeros = []

while True:
    n = int(input('Escreve um número> '))

    if n not in numeros:
        numeros.append(n)

    else:
        print('O número {:.0f} já está lista!'.format(n))
        break

if 5 not in numeros:
    print(f'\nForam digitados {len(numeros)} número/s.\nO número 5 não está na lista.\nLista em ordem decrescente:', end=' ')
    
    for i in numeros:
        print(i, end=', ')

else:
    print(f'\nForam digitados {len(numeros)} número/s\nO número 5 está na lista.\nLista em ordem decrescente:', end=' ')
    
    for i in numeros:
        print(i, end=', ')

print()