altura = float(input('Escreve a tua altura> '))
peso = float(input('Escreve o teu peso> '))
peso = peso / altura ** 2

cores = {'vazio':'\033[m',
         'roxo':'\033[1;35m',
         'verde':'\033[1;32m',
         'laranja':'\033[1;33m',
         'vermelho':'\033[1;31m'}

if peso < 18.5:
    print('Tu estás {}Abaixo do Peso{}.\nIMC {}{:.2f}{}.'.format(cores['roxo'], cores['vazio'], cores['roxo'], peso, cores['vazio']))

elif peso >= 18.5 and peso <= 25:
    print('Tu estás com {}Peso Ideal{}.\nIMC {}{:.2f}{}.'.format(cores['verde'], cores['vazio'], cores['verde'], peso, cores['vazio']))

elif peso >= 25 and peso <= 30:
    print('Tu estás com {}Sobrepeso{}.\nIMC {}{:.2f}{}.'.format(cores['laranja'], cores['vazio'], cores['laranja'], peso, cores['vazio']))

elif peso >= 30 and peso <= 40:
    print('Tu estás com {}Obesidade{}.\nIMC {}{:.2f}{}.'.format(cores['vermelho'], cores['vazio'], cores['vermelho'], peso, cores['vazio']))