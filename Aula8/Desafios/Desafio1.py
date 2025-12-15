casa = float(input('Qual é o preço da casa que pretendes comprar?> '))
anos = int(input('Em quantos anos pretendes pagar o emprestimo?> '))
salario = float(input('Quanto ganhas por mês?> '))

cor = {'Limpa':'\033[m',
       'verde':'\033[1;32m',
       'vermelho':'\033[1;31m'}

if (salario * 0.3) * (12 * anos) - casa >= 0:
    print('{}Emprestimo Autorizado!{}'.format(cor['verde'], cor['Limpa']))
else:
    print('{}Emprestimo Não Autorizado!{}'.format(cor['vermelho'], cor['Limpa']))