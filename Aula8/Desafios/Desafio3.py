n1 = int(input('Escreve um número inteiro> '))
n2 = int(input('Escreve mais um número inteiro> '))

cores = {'sem':'\033[m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'cinzento':'\033[1;37m'}

if n1 > n2:
    print('{}{}{} é maior que {}{}{}'.format(cores['azul'],n1,cores['sem'],cores['cinzento'],n2,cores['sem']))
elif n1 < n2:
    print('{}{}{} é menor que {}{}{}'.format(cores['cinzento'], n1, cores['sem'], cores['amarelo'], n2, cores['sem']))
else:
    print('{}{}{} é igual a {}{}{}'.format(cores['cinzento'], n1, cores['sem'], cores['cinzento'], n2, cores['sem']))