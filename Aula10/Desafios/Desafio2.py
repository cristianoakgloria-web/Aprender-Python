from random import randint
n = int(input('Tenta adivinhar o número de 0 a 10> '))
pc = randint(0, 10)
cont = 0

while pc != n:
    n = int(input('Erraste, tenta outra vez(0/10)> '))
    cont += 1

print('Acertaste, parabens!\nNúmero de tentativas:', cont)