matriz = [[int(input('Número> '))], [int(input('Número> '))], [int(input('Número> '))], [int(input('Número> '))], [int(input('Número> '))], [int(input('Número> '))], [int(input('Número> '))], [int(input('Número> '))], [int(input('Número> '))]]
i = 0
while i < len(matriz):
    print(matriz[i], end=' ')
    i += 1
    if i%3 == 0:
        print()