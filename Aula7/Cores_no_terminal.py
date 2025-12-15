nome = 'Steve'
cor = '\033[7;30mOlá\033[m' # Bold, texto preto, Fundo lilás
cores = {'limpa':'\033[m',
       'azul':'\033[34m',
       'pretobranco':'\033[7;30m'}
print('apresentação 1: {}{}{}\n apresentação 2 : {}'.format(cores['azul'], nome, cores['limpa'], cor))