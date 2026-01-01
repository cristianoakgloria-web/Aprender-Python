def leiaInt(n):
    try:
        return int(n)
    except ValueError:
        print('O valor fornecido não é do tipo número!')

n = leiaInt(input('Escreve um número> '))
print(n)