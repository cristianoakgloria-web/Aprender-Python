desempenho = {'Nome':str(input('Digite o nome do jogador> ')), 'Njogos':int(input('Digita um número de jogos participados> '))}
golos = 0
for c in range(0, desempenho['Njogos']):
    desempenho[f'Ngolos{c + 1}'] = int(input(f'Quantos golo no jogo {c + 1}?> '))
    golos += desempenho[f'Ngolos{c + 1}']
print(f'\nNúmero total de golos do jogador {desempenho["Nome"]}: {golos}.\nParticipação em {desempenho["Njogos"]} jogos.\nMédia de golos por jogo: {golos/desempenho["Njogos"]}')