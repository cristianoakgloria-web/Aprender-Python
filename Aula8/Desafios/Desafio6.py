nascimento = int(input('Escreve o ano de nascimento do Atleta> '))

cor ={'sem':'\033[m',
      'azul':'\033[1;34',
      'amarelo':'\033[1;33m',
      'verde':'\033[1;32m',
      'ciano':'\033[1;36m',
      'vermelho':'\033[1;31m'}

if (2025 - nascimento) <= 9:
    print('Atleta {}Miúdo{}'.format(cor['ciano'],cor['sem']))

elif (2025 - nascimento) <= 14:
    print('Atleta {}Infatil{}'.format(cor['azul'],cor['sem']))

elif (2025 - nascimento) <= 19:
    print('Atleta {}Junior{}'.format(cor['verde'],cor['sem']))

elif (2025 - nascimento) <= 20:
    print('Atleta {}Sênior{}'.format(cor['amarelo'],cor['sem']))

else:
    print('Atleta {}MASTER{}'.format(cor['vermelho'], cor['sem']))