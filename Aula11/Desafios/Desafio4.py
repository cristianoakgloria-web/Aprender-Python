nF20 = 0
n18 = 0
nM = 0
while True:
    idade = int(input('Idade> '))

    while True:
        sexo = input('Sexo (F/M)> ').upper()
        if sexo == 'F' or sexo == 'M':
            break

    if sexo in 'F' and idade < 20:
        nF20 += 1

    elif sexo in 'M':
        nM += 1

    if idade > 18:
        n18 += 1

    sN = input('Queres continuar(S/N)?> ').upper()

    if sN not in 'S':
        break

print(f'Quantidade de mulheres com menos de 20 anos: {nF20:.0f}.\n'
      f'Quantidade de homens: {nM:.0f}.\n'
      f'Quantidade de pessoas com mais de 18 anos: {n18:.0f}.')