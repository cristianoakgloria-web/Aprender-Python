new18 = 0
old18 = 0
for i in range(1, 7 +1):
    idade = int(input('Escreve a Idade> '))
    if idade == 18:
        new18 += 1
    elif idade > 18:
        old18 += 1

print('Das {} pessoas, {} têm 18 e {} têm mais de 18.'.format(i, new18, old18))