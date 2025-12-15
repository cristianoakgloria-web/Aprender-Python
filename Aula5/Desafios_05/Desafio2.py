n = int(input('Escreve um número de 0 a 9999> '))
n2 = str(n)
n2 = n2.replace('', ' ')
n2 = n2.split()

if (n < 10000 and n > -1):
        if (n < 10000 and n >= 1000):
            print('unidade: {}\ndezena: {}\ncentena {}\nmilhar {}'.format(n2[0], n2[1], n2[2], n2[3]))

            if (n < 1000 and n >= 100 ):
                    print('unidade: {}\ndezena: {}\ncentena {}'.format(n2[0], n2[1], n2[2]))

                    if(n < 100 and n >= 10):
                        print('unidade: {}\ndezena: {}'.format(n2[0], n2[1]))

                        if (n < 10):
                            print('unidade: {}'.format(n2[0]))



