numeros = []
crescente = []

while True:
    n = int(input('Escreve um número> '))

    if n not in numeros:
        numeros.append(n)

    else:
        print('O número {:.0f} já está lista!'.format(n))
        break

print('Lista em ordem crescente: ', end=' ')
while numeros:
    n = numeros[0]

    for c in numeros:
        if(n < c):
            n = c
            
    crescente.insert(0, n)
    numeros.remove(n)

del numeros

for c in crescente:
    print(c, end=' ')
    
print()