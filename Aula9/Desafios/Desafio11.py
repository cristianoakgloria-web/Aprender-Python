old = 0
media = 0
mulheres = 0
for i in range(1, 4 + 1):
    nome = input('Nome> ')
    idade = int(input('Idade> '))
    sexo = input('Sexo(F/M)> ')

    media += idade

    if sexo in 'F':
        mulheres += 1
    if old == 0 or old < idade:
        old = idade
        oldname = nome

media = media / i
print('A pessoa mais velha é {} com {} ano/s, tem {} mulheres e a média de todas as idades é {} ano/s'.format(oldname, old, mulheres, media))