jogadores = list()
while True:
    c = 'S'
    golos = 0
    jogador = {'Jogador':str(input('Nome do jogador> ')), 'Participações':int(input('Número de jogos participados> '))}
    for a in range(0, jogador['Participações']):
        jogador[f'Ngolos{a + 1}'] = int(input(f'Quantos golos no jogo {a + 1}?> '))
        golos += jogador[f'Ngolos{a + 1}']
    jogador['Golos'] = golos
    jogadores.append(jogador.copy())
    c = str(input('Continuar(S/n)?> '))
    if c != 'S':
        break

op = -1
i = 0
while True:
    c = 'S'
    i = 0
    for jg in jogadores:
        for k, v in jg.items():
            if k == 'Jogador':
                print(f'{i + 1}-{v}.')
                i += 1
    op = int(input('Escolhe um número para ver o desempenho de um jogador.\n> ')) - 1
    if op > len(jogadores) or op < len(jogadores):
        print(f'\nNúmero total de golos do jogador {jogadores[op]["Jogador"]}: {jogadores[op]["Golos"]}.\nParticipação em {jogadores[op]["Participações"]} jogos.\nMédia de golos por jogo: {jogadores[op]["Golos"]/jogadores[op]["Participações"]}')
    c = str(input('Continuar(S/n)?> '))
    if c != 'S':
        break