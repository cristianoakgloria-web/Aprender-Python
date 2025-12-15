from random import randint
escolha = int(input('Pedra-1\nPapel-2\nTesoura-3\n> '))
escolha_pc = randint(1, 3)

if escolha == escolha_pc:
    print('Empate')

elif escolha == 1 and escolha_pc == 2:
    print('Computador Venceu!')

elif escolha == 2 and escolha_pc == 1:
    print('Tu Venceste!')

elif escolha == 2 and escolha_pc == 3:
    print('Computador Venceu!')

elif escolha == 3 and escolha_pc == 2:
    print('Tu Venceste!')

elif escolha == 3 and escolha_pc == 1:
    print('Computador Venceu!')

elif escolha == 1 and escolha_pc == 3:
    print('Tu Veenceste!')