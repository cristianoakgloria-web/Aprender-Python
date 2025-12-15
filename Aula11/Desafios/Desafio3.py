import random

n = int(input('Escreve um número inteiro de 0 a 5> '))
ni = 0
count = 0

while True:
# while secundario
# Autentucaçoã dos inputs

    while True:
        if ni != 0:
            n = int(input('Escreve um número inteiro de 0 a 5> '))
            ni = 0

        elif 0 <= n <= 5:
            paridade = input('Escolha Par(P) ou Ímpar(I)> ').upper()
            if paridade in 'P' or paridade in 'I':
                break

        else:
            n = int(input('Escreve um número inteiro de 0 a 5> '))
            ni = 0

# while princípal
# input da máquina e calculo do resto

    pc = random.randint(0, 5)
    print(f'Computador escolheu: {pc}')
    m = (n + pc) % 2

# condições para vitória e derrota

    if m == 0 and paridade in 'P':
        print('Ganhaste!')
        ni = 1
        count += 1

    elif m !=0 and paridade in 'I':
        print('Ganhaste!')
        ni = 1
        count += 1

    else:
        print('Gamae Over!')
        break

print(f'Número de vitórias: {count}')