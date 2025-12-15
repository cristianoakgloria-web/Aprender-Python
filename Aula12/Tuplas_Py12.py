# Tuplas são variávis compostas
# As tuplas são imutaveis
lanches = 'Hambúrguer', 'Sumo de manga', 'Pizza', 'Fanta laranja'
sobremesas = ('Musse de chocolate', 'Pundin', 'Uma fatia de bolo')

print(lanches[-1:]) # Mostra o último elemento
print(lanches[1:2]) # Mostra dois elementos específicos
print(len(lanches)) # Mostra o tamanho da variável composta
print(lanches [:3]) # Mostra do primeiro elemento até o terceiro
print(lanches[0:]) # Mostra todos elementos apartir de uma posição
print(sorted(lanches)) # Mostra os elementos da variável composta em ordem alfabetica
print(lanches.index('Pizza')) # Diz em que posição está um determinado elemento
menu = lanches + sobremesas # cria um nova tupla apartir da junção de outras duas
del(sobremesas)  # elemina completamete uma tuplas específica na memória do computador em quanto o código está em execução
print(menu)

# Percorre cada elemento da variável composta
for c in lanches:
    print(c)

for c in range(0, len(lanches)):
    print(lanches[c])

for b, c in enumerate(lanches):
    print(b, ' - ', c)