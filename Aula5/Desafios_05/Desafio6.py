nome = input('Nome completo> ')
nome1 = nome.split()
nome = len(nome1)

if(nome > 1):
    print('Primeiro nome: {}\nÚltimo nome: {}'.format(nome1[0], nome1[nome-1]))