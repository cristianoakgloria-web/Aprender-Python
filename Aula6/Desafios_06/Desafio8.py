x = float(input('Escreve o comprimento da linha x> '))
y = float(input('Escreve o comprimento da linha y> '))
z = float(input('Escreve o comprimento da linha z> '))

if x == y == z:
    print('O comprimento das linhas é o suficiente para formar um triângulo equilátero!')
if (x ** 2 + y ** 2) ** 0.5 == z:
    print('O comprimento das linhas é o suficiente para formar um triângulo retângulo!')
else:
    print('O comprimento das linhas não formam um triângulo equlátero ou triângulo retângulo!')