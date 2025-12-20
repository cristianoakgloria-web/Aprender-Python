def escreve(txt):
    # Solução maís eficiente
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))

    # A minha primeira solução
#    t = 0
#    while True:
#        if t < len(txt) + 4:
#            print('~', end='')
#            t += 1

#        elif len(txt) + 4 <= t < (len(txt) + 4) * 2:
#            print(f'\n  {txt} ')
#            t = (len(txt) + 4) * 2
            
#        elif (len(txt) + 4) * 2 <= t < (len(txt) + 4) * 3:
#            print('~',end='')
#            t += 1

#         else:
#            print()
#            break

t = input('Escreve algo> ')
escreve(t)