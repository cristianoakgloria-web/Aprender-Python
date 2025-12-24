cores = {'sem':'\033[m',
         'azul':'\033[1;30;44m',
         'branco':'\033[1;35m'}


def manual(c):
    import pydoc
    print(cores['azul'])
    print(pydoc.render_doc(c))
    print(cores['sem'])

while True:
    print(cores['branco'])
    h = input('Escreve uma função ou biblioteca ou FIM para encerrar> ')
    print(cores['sem'])
    if h.upper() in 'FIM':
        break
    else:
         manual(h)