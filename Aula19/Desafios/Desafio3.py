def título(texto):
    print()
    print('─' * 50)
    print(' ' * int(25 - (len(texto) / 2)), texto)
    print('─' * 50)

while True:
    título('Mini-Sistema de Lista de Pessoas')
    print('  1 ─ Cadastrar nova pessoa.\n  2 ─ Lista de pessoas\n  0 ─ Sair.')
    op = int(input('\nEscolha uma opcção> '))

    if op == 2:
        lista = []
        título('Lista de Pessoas')
        with open('Desafio3_Aula19.txt', 'r') as pessoas:
            for linha in pessoas:
                lista.append(linha.replace('\n', ''))

        for n in range(1, len(lista) + 1):
            if (n % 2) == 0:
                print('.' * int(38 - len(lista[n - 2])), end='')

                try:
                    if int(linha[n - 1]) > 1:
                        print(lista[n - 1], 'anos')
                    else:
                        print(lista[n - 1], 'ano')
                except:
                    if int(lista[n - 1]) > 1:
                        print(lista[n - 1], 'anos')
                    else:
                        print(lista[n - 1], 'ano')
                        
            else:
                print('  ', lista[n - 1], end='')
        input()

    elif op == 1:
        título('Cadastrar Nova Pessoa')
        nome = str(input('Escreve a nome> '))

        while True:
            idade = str(input('Escrece a idade> '))

            try:
                if int(idade):
                    with open('Desafio3_Aula19.txt', 'a') as pessoa:
                        pessoa.write(nome + '\n')
                        pessoa.write(idade + '\n')
                    break
            except (ValueError, TypeError):
                print('Erro: Idade deve ser um número inteiro!')
        input()

    elif op == 0:
        break

    else:
        print('Opcção Inválida!')
        input()