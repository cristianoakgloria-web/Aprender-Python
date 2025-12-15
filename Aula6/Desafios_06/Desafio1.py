import random
n = int(input('Adivinha qual é o número certo(0 a 5)> '))
nc = random.randint(0, 5)

if n == nc:
    print('Acertaste!')

else:
    print('Erraste, mais sorte para próxima!')