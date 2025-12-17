pessoas = [[input('Nome> '), float(input('Peso> '))], [input('Nome> '), float(input('Peso> '))], [input('Nome> '), float(input('Peso> '))], [input('Nome> '), float(input('Peso> '))]]
leves = []
pesadas = []
media = 0

for p in pessoas:
    media += p[1]
media = int(media / len(pessoas))

for p in pessoas:
    if media > p[1]:
        leves.append(p[:])
    else:
        pesadas.append(p[:])

print('As pessoas mais leves: ', end='')
for leve in leves:
    print(leve[0], end=' ')

print('\nAs pessoas mais pessadas: ', end='')
for pesada in pesadas:
    print(pesada[0], end=' ')
print()