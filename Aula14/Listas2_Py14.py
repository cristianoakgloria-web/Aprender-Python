teste = list()
teste.append('Duarth')
teste.append(17)

pessoas = [['Ana', 18], ['Pedro', 20]]
pessoas.append(teste[:])

teste[0] = 'Marria'
teste[1] = 16

pessoas.append(teste[:])

print(pessoas)
print(pessoas[0])
print(pessoas[1][1])

pessoas.clear()

for pessoa in pessoas:
    print(pessoa[0], pessoa[1])