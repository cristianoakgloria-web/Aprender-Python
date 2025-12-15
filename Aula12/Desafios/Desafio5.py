tupla = ('Telefone', 34500, 'Tablet', 120000, 'Notebook', 230000)
cc = 0

for c in range(0, len(tupla)):
    if cc + 2 < len(tupla):
        print('{:.<30}AOA$ {}'.format(tupla[cc],tupla[cc + 1]))
        cc+=2

print('{:.<30}AOA$ {}'.format(tupla[cc],tupla[cc + 1]))