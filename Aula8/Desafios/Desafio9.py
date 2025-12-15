preco = float(input('Escreve o preço original do produto> '))
pagamento = int(input('Qual é a forma de pagamento\nÀ vista dinheiro/cheque 1\nÀ vista no cartão 2\nAté 2x no cartão 3\n3x ou mais no cartão 4\n> '))

cores = {'vazio':'\033[m',
         'verde':'\033[1;32m',
         'laranja':'\033[1;33m',
         'vermelho':'\033[1;31m'}

if pagamento == 1:
    print('Tu ganhaste 15% de desconto.\nNovo preço: AOA {}{:.2f}{}'.format(cores['verde'], preco - (preco * 0.15), cores['vazio']))

elif pagamento == 2:
    print('Tu ganhaste 15% de desconto.\nNovo preço: AOA {}{:.2f}{}'.format(cores['verde'], preco - (preco * 0.05), cores['vazio']))

elif pagamento == 3:
    print('Tu não ganhaste nenhum desconto.\nPreço: AOA {}{:.2f}{}'.format(cores['laranja'], preco, cores['vazio']))

elif pagamento == 4:
    print('Tu sofreste 25% de juro.\nNovo preço: AOA {}{:.2f}{}'.format(cores['vermelho'], (preco * 0.25) + preco, cores['vazio']))