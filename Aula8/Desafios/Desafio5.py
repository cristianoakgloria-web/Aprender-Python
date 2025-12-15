nota1 = float(input('Escreve a primeira nota do aluno> '))
nota2 = float(input('Escreve a segunda nota do aluno> '))

cores = {'sem':'\033[m',
         'vermelho':'\033[1;31m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m'}

if ((nota1 + nota2) / 2) < 5:
    print('Aluno {}Reprovado{}!'.format(cores['vermelho'], cores['sem']))

elif ((nota1 + nota2) / 2) >= 5 and ((nota1 + nota2) / 2) <= 6.9:
    print('Aluno em {}Recuperação{}!'.format(cores['azul'], cores['sem']))

else:
    print('Aluno {}Aprovado{}!'.format(cores['verde'], cores['sem']))