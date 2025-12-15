linha1 = float(input('Ecreve o comprimrnto da 1º linha> '))
linha2 = float(input('Ecreve o comprimrnto da 2º linha> '))
linha3 = float(input('Ecreve o comprimrnto da 3º linha> '))

cores = {'vazio':'\033[m',
         'amarelo':'\033[1;33m',
         'verde':'\033[1;32m',
         'azul':'\033[1;34m'}

if linha1 == linha2 and linha2 == linha3:
    print('{}Triâgulo Equilátero{}'.format(cores['amarelo'], cores['vazio']))

elif linha1 == linha2 and linha2 != linha3 or linha1 == linha3 and linha3 != linha2 or linha2 == linha3 and linha3 != linha1:
    print('{}Triângulo Isósceles{}'.format(cores['verde'], cores['vazio']))

elif linha1 != linha2 and linha2 != linha3:
    print('{}Triângulo Escaleno{}'.format(cores['azul'], cores['vazio']))
