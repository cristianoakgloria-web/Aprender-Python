n = 753 #int(input('Escreve um número inteiro> '))
converter = 3 #int(input('1 - para binário.\n2 - para octal.\n3 - para hexadecimal.\nEscolhe uma das opcções para converteção> '))

cores = {'Limpa':'\033[m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m'}

if converter == 1:
    print()
elif converter == 2:
    print()
elif converter == 3:
    print()
else:
    print('{}Opcção Inválida!{}'.format(cores['vermelho'], cores['Limpa']))