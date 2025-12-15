frase = input('Frase> ')

print('A letra "A" aparece pela primeira vez na posição: {}\nE pela última vez na posição '.format(frase.find('A')))
if(frase.count('A') == 1):
    print('A letra "A" aparece: 1 vez')
else:
    print('A letra "A" aparece: {} vezes'. format(frase.count('A')))