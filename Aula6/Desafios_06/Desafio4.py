km = int(input('Quantos Km a viagem teve?> '))

if km > 200:
    print('O preço do bilhete é de AOA${:.2f}'.format(km * 50))
else:
    print('O preço do bilhete é de AOA${:.2f}'.format(km * 45))