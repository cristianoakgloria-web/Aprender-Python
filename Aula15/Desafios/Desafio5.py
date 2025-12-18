pessoas = list()
while True:
    b = 'S'
    pessoa = {'Nome':str(input('Nome> ')), 'Idade':int(input('Idade> ')), 'Sexo':str(input('Sexo(F/M)> '))}
    if pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
        print('Formato do Sexo errado!')
    else:
        pessoas.append(pessoa.copy())
        b = str(input('Continuar(S/n)?> '))
    if b != 'S':
        break
print(f'\nNúmero de pessoas cadastradas: {len(pessoas)}')

media = 0
mulheres = list()
cimamédia = list()
for p in pessoas:
    for k, v in p.items():
        if k == 'Idade':
            media += v
        if k == 'Sexo':
            if v == 'F':
                mulheres.append(p.copy())
media/=len(pessoas)

for p in pessoas:
    for k, v in p.items():
        if k == 'Idade':
            if v > media:
                cimamédia.append(p.copy())
print(f'A média de idades: {media}\nLista de mulheres: {mulheres}\nLista de pessoas com a idade maior que a média: {cimamédia}')