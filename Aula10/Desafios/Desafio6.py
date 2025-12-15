n = int(input('Escreve a quantidade que quer> '))
while n != 0:
    for i in range(1, n):
        if i % 2:
            print(i)
    n = int(input('Escreve a quantidade que quer> '))