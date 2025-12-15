total =0
caros = 0
barato = ''
bar = 0
i = 1

while True:
    nome = input('Nome do produto> ')
    preco = float(input('Preço> '))

    if 0 >= bar or bar >= preco:
        barato = nome
        bar = preco

    if preco > 100000:
        caros += 1

    total += preco

    if i % 3 == 0:
        end = input('Continuar(S/N)?> ').upper()

        if end in 'N':
            break

    i += 1

print(f'Produto mais barato: {barato}.\nQuantidade de produtos com preço superior a AOA$100mil: {caros:.0f}\nTotal gasto: AOA${total:.2f}')