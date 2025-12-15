frase = input('Escreveuma frase sem acentos e pontuação> ')
frase2 = frase

frase = frase.replace(' ', '').lower()

m = len(frase)
c = 0

if m % 2:
    for i in range(0, m):
        if frase[i] != frase[(m-1) - i] and i >= (m-1)/2:
            c = 1
    if c == 0:
        print('A frase "{}" é palíndroma!'.format(frase2))
    else:
        print('A frase "{}" não é palíndroma!'.format(frase2))

else:
    for i in range(0, m):
        if frase[i] != frase[(m-1) - i]:
            c = 1
    if c == 0:
        print('A frase "{}" é palíndroma!'.format(frase2))
    else:
        print('A frase "{}" não é palíndroma!'.format(frase2))