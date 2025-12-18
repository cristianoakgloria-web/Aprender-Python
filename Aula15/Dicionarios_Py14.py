dicionario = {'Nome':'Ana',
               'Idade':'19'}
# Ou dicionario = dict()
#print(dicionario['nome'])

dicionario['Sexo'] = 'F' # Cria a chave 'Sexo'
del dicionario['Idade'] # Elimina a chave 'Idade'

print(dicionario.items()) # Mostra os as chaves e valores
print(dicionario.keys()) # Mostra todas as chaves
print(dicionario.values()) # Mostra todos os valores

for k, v in dicionario.items():
    print(f'{k}: {v}')
    
província = dict()
angola = list()

for p in range(0, 2):
    província['Província'] = str(input('Província> '))
    província['Sigla'] = str(input('Sigla> '))
    angola.append(província.copy())

    
for a in angola:
    for k, v in a.items():
        print(f'{k} = {v}')

for a in angola:
    for v in a.values():
        print(v)