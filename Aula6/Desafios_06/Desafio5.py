ano = int(input('Escreve um ano> '))
print('O ano {:.0f}, é um ano bissexto!'.format(ano) if ano%4 == 0 else 'O ano {:.0f}, não é um ano bissexto!')