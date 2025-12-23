# Interactive Help
# O __doc__ e o help() servem para acessar a documentação de objetos (módulos, funções, classes ou métodos)
#help()
#print(.__doc__)


# docstrings
# docstrings, basicamente para criar um manual de uma função criada
def contador(i, f, p):
    """
    Faz um contagem e mostra na tela.
    :param i: ínicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    while i <= f:
        print(f'{i}', end=' ')
        i += p
#help(contador) # mostra o manual da função contador()


# Argumentos opcionais
def somar(a=0, b=0, c=0):
    print(f'{a} + {b} + {c} = {a + b + c}')
somar(2, 3, 3)
somar(5, 3)
somar()


# Escopo de variáveis
# temos o variável global, variável local
# temos funções importadas globais e locais
def teste(b):
    global a # usa o A global e não o local
    a = 1 # este A é uma variável local
    b += 4 # o B é uma variável local
    c = 2 # o C é uma variável local
    print(f'\nA vale {a}\nB vale {b}\nC vale {c}')
a = 5 # este A é um variável global
teste(a)


# Retorno de resultados
# as variáveis podem retornar ou não valores
def soma(a, b, c):
    return a + b + c
resposta = soma(2, 3, 4)
print(f'\n{resposta}')