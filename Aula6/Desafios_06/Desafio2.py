velocidade = float(input('Qual é a tua velocidade actual?> '))

if velocidade > 80:
    print('Tu estás a {}Km/h e a tua multa é de AOA${:.2f}'.format(velocidade, (velocidade - 80) * 700))