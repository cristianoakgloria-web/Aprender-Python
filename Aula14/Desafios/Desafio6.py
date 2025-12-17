alunos = [[input('Nome> '), float(input('Nota1> ')), float(input('Nota2> '))], [input('Nome> '), float(input('Nota1> ')), float(input('Nota2> '))], [input('Nome> '), float(input('Nota1> ')), float(input('Nota2> '))], [input('Nome> '), float(input('Nota1> ')), float(input('Nota2> '))]]
mediatotal = 0

for a in range(0, len(alunos)):
    mediatotal += alunos[a][1] + alunos[a][2]
mediatotal /= (len(alunos) * 2)


print(f'A média total de todos os alunos é {mediatotal}')
while True:
    print('\nEscolha uma opcção.\nVer a média do aluno/a:')
    for b in range(0, len(alunos)):
        print(f'{b + 1}-{alunos[b][0]}')
    print('Sair: -1')
    op = int(input('> ')) - 1

    if op <= -1 or op >= len(alunos):
        break
    else:
        print(f'A media do/a aluno/a {alunos[op][0]}: {(alunos[op][1] + alunos[op][2])/2}')
        input()