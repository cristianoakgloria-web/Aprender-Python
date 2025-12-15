n1 = float(input('Escreve um número> '))
n2 = float(input('Escreve mais um número> '))
op = int(input('Escolha uma opcção\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n> '))
fim = 1
while fim == 1:
    if op == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))

    elif op == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))

    elif op == 3:
        if n2 < n1:
            print('{} > {}'.format(n1, n2))
        elif n1 < n2:
            print('{} < {}'.format(n1,n2))
        else:
            print('{} = {}'.format(n1,n2))

    elif op == 4:
        n1 = float(input('Escreve um número> '))
        n2 = float(input('Escreve mais um número> '))

    elif op == 5:
        fim = 0

    else:
        print('OPCÇÃO INVALIDA!')

    if fim != 0:
        op = int(input('Escolha uma opcção\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n> '))