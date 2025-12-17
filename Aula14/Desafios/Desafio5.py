from random import randint
ngames = int(input('Quatos jogos serão gerados?> '))
sorteios = []

for a in range(0, ngames):
    palpite = list()
    for b in range(0, 5):
        palpite.append(randint(0, 100))
    sorteios.append(palpite[:])

print('Os números sorteados são: ')
for c in range(0, len(sorteios)):
    print(f'Jogo{c + 1}: {sorteios[c]}')