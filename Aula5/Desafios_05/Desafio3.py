cidade = input('Escreve o nome de uma cidade> ')
cidade2 = cidade.lower()

if(cidade2.count('h') == True):
    print('A cidade {} começa com "H".'.format(cidade))
else:
    print('A cidade {} não começa com "H".'.format(cidade))