matriz = [[int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))],[int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))], [int(input('Escreve um número> '))]]
i = 0
soma = 0
maior = 0
soma3linha = 0

while i < len(matriz):
    print(matriz[i], end=' ')

    soma += matriz[i][0]
    if i >= 6 and i < 9:
        soma3linha += matriz[i][0]

    if i >= 4 and i <6:
        if maior <= i:
            maior = matriz[i][0]
    i += 1
    if i%3 == 0:
        print()

print(f'A soma de todos os números: {soma}\nO maior número da segunda linha: {maior}\nA soma de todos os números da terceira linha: {soma3linha}')