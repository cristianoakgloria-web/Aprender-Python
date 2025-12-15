cd = 0
rmoney = 0
money = int(input('Quantidade a levantar> '))

while True:
    if money >= 5000:
        rmoney += 5000
        money -= 5000
        cd +=1

    elif money >= 2000:
        rmoney += 2000
        money -= 2000
        cd += 1

    elif money >= 500:
        rmoney += 500
        money -= 500
        cd += 1

    elif money >= 200:
        rmoney += 200
        money -= 200
        cd += 1

    elif money < 200:
        break

print(f'Quatidade de cédulas levantadas: {cd:.0f}.\nValor permitido para levantar: AOA${rmoney:.2f}')