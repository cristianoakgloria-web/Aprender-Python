from random import shuffle

aluno1 = 'Ana'
aluno2 = 'Paulo'
aluno3 = 'Luíza'
aluno4 = 'Martins'

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print('A ordem de apresentação é:\n {}'.format(lista))