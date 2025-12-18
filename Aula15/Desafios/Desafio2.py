from random import randint
dados = {'Dado1':randint(1,6), 'Dado2':randint(1,6), 'Dado3':randint(1,6), 'Dado4':randint(1,6)}
maior = 0
dado = ''
for k, v in dados.items():
    if maior < v:
        dado = k
        maior = v
print(f'O jogador do {dado} é o vencerdor, valor do dado: {maior}')