m = 0
count = 0
while True:
    n = int(input('Escreve um número inteiro> '))
    if n == 999:
        break
    else:
        m += n
        count += 1
print(f'Foram digitados {count} número/s e a soma de todos eles é {m}.')