tupla = (int(input('Escreve um número> ')), 
         int(input('Escreve um número> ')),
         int(input('Escreve um número> ')),
         int(input('Escreve um número> ')))

print('Os números pares:', end=' ')

for c in range(0, len(tupla)):
    if tupla[c]%2 == 0:
        print(tupla[c], end=' ')

print('\nO primeiro número 3 está na posição: {}\nO número 9 apareceu {} vezes.'.format(tupla.index(3), tupla.count(9)))