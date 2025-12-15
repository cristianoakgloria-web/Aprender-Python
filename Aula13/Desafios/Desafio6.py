expreção = input('Escreve um operação que comece e termine em parênteses> ')
lista = []
for c in expreção:
    if c in '(':
        lista.append(1)    
    elif c in ')' and len(lista) > 0:
        lista.pop()
if len(lista) == 0:
    print('A expressão está certa!')  
else:
    print('Expressão Errada!')