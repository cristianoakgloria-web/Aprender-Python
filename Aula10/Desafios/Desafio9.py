end = 'S'
count = 0
maior = 0
menor = 0
media = 0
breakk = 2
while end != 'N':
    n = int(input('Escreve um valor> '))
    media = media + n

    if maior < n:
        maior = n

    if menor > n:
        menor = n

    if count >= breakk:
        end = input('Quer continuar?(S/N)> ').upper()
        breakk += 3

    count += 1

print('A média dos números é {}, o maior número é {} e o menor é {}'.format(media/count, maior, menor))