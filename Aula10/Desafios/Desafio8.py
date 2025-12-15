m = int(input('Escreve um número> '))
count = 1
n = 0
while n != 999:
    n = int(input('Escreve um número> '))

    if n != 999:
        m += n
        count += 1

print ('Foram digitados {} número/s e a soma de todos os números digitados é: {}'.format(count, m))