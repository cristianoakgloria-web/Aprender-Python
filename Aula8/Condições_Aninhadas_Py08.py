nome = input('Escreve o teu nome> ')

if nome in 'Nala' or nome == 'Emília' or nome in 'Diara' or nome in 'Nia':
    print('{} é um nome lindo para meninas!'.format(nome))
elif nome in 'Amir' or nome in 'Akin' or nome in 'Francisco':
    print('{} é um nome lindo para meninos!'.format(nome))
else:
    print('{}?\nOk'.format(nome))
print('Tenha um ótimo dia, {}.'.format(nome))