from random import randint

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0,100), randint(0,100))

print('Os números gerados são: ', end=' ')

for c in range(0, len(tupla)):
    print(tupla[c], end=' ')

print(f'\nO maior número é {max(tupla)}.\nE o menor é {min(tupla)}.')