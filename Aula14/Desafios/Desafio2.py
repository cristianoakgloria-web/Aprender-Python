numeros = [[int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))]]
pares = []
ímpares = []

for i in numeros:
    if i[0]%2:
        ímpares.append(i[:])
    else:
        pares.append(i[:])
    
print('Os números pares: ', end='')
for par in pares:
    print(par[0], end=' ')

print('\nOs números ímpares: ', end='')
for ímpar in ímpares:
    print(ímpar[0], end=' ')
print()