# Crianção de Listas
numeros = list(range(0,10+1)) # Criar uma lista de números de 0 até 10 em ordem
menu = ['Muamba de Galinha', 'Bitoque', 'Prego no Prato'] # Criar um lista manualmente

# Adicionar Novos Elementos na Lista
menu.append('Mufete') # Adiciona um novo elemento no fim da lista
menu.insert(0,'Muce de Chocolate') # Adiciona um novo elemeto em uma posição específica da lista

# Eliminar Elementos da Lista
del menu[4] # Elimina um elemento da lista pela posição
menu.pop(0) #  Elimina um elemento da lista pela posição
menu.remove('Prego no Prato') # Elimina um elemento da lista pelo "nome"

# Outras Manipulações para Listas
menu.sort() # Organiza as listas de forma crescente ou alfabetica

# Cópia de Listas
a = numeros[:] # Cria uma cópia de uma lista
b = numeros # Cria um ligaçõa directa com uma lista
b[3] = 32

numeros.sort(reverse=True) # Organiza as listas de forma decrescente
print(menu, '\n', numeros, '\n', b, '\n', a)