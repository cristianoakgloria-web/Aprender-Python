def contador(start, end, step):
    if start > end:
        start += step
        for i in range(start, end + step, -1):
            if i % step == 0:
                start -= step
                print(start, end=' ')
        print()

    elif start < end:
        start -= step
        for i in range(start, end):
            if i % step == 0:
                start += step
                print(start, end=' ')
        print()

contador(1, 10, 1)
contador(10, 1, 2)

a = input('Deseja fazer uma contagem personalizada(S/n)?> ').upper

if a == 'S':
    a = int(input('Número para o ínicio da contagem> '))
    b = int(input('Número para o final da contagem> '))
    c = int(input('Número de intervalo> '))

    contador(a, b, c)