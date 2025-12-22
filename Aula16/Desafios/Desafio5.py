from random import randint
def somarPar(n):
    pares = 0
    for i in range(0, len(n)):
        if n[i] % 2 == 0:
            pares += n[i]
    print(f'A soma dos números pares: {pares}')

def sorteia():
    números = list()
    for i in range(0, 5):
        números.append(randint(0, 101))
    return somarPar(números)
   
sorteia()