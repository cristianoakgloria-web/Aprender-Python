def ficha(nome = '', golos = '0'):
    """
    Função para imprimir a ficha de um jogador
    
    :param nome: Nome do jogador
    :param golos: A quantidade de golos feitos pelo mesmo jogador
    :return: retorna um argumento com nome e a quantidade
    """
    return f'{"~" * (len(nome) + len(golos) + 39)}\n  O jogador {nome}, fez um total de {golos} golos.\n{"~" * (len(nome) + len(golos) + 39)}'

nome = input('Escreve o nome do jogador> ')
while True:
    golos = input(f'Escreve a quantidade de golos feito pelo jogador {nome}> ')
    if golos in '' or golos.isdecimal():
        break
print(ficha(nome, golos))