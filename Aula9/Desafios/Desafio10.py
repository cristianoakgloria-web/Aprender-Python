pesoleve = 0
pesopesado = 0

for i in range(1, 5 + 1):
    peso = float(input('Escreve o pesso> '))

    if pesoleve ==0 or pesoleve > peso:
        pesoleve = peso
    if pesopesado == 0 or pesopesado < peso:
        pesopesado = peso

print('Dos {} pesos lidos, {} foi o maior peso e {} o menor!'.format(i, pesopesado, pesoleve))