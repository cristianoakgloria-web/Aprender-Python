frase = ' Manipular este Texto '
print('este' in frase) # Verifica se existe uma determinada sequencia de caraceres na variavél do tipo str
print(frase.count('e', 0, 13)) # conta quantos vezes uma determinada sequência de caracteres aparece em uma variavél do tipo str em um intervalo de caracteres
print(frase.find('tex')) # Diz em posição está uma determinada sequência de caracteres apartir de um intervalo de posições
print(len(frase)) # Diz o tamanho de uma variavél do tipo str
print(frase.replace('este', 'neste')) # subistitui uma sequecia de caracteres de uma variavél do tipo str e substitui por uma nova
print(frase.upper()) # torna todos caracteres de minusculas para maiusculas
print(frase.lower()) # torna todos caracteres de maiusculas para minusculas
print(frase.capitalize()) # torna todos caracteres de minusculas para maiusculas, menos o primeiros caracter
print(frase.title()) # torna os primeiros caracteres de cada palavra em maiuscula
print(frase.strip()) # remove os espaços no ínicio e no final
print(frase.rstrip()) # remoce os espaços a direita
print(frase.lstrip()) # remove os espaços a esquerda
print(frase.split()) # faz uma divisão apartir dos espaços e +
print(' '.join(frase)) # separa cada caracter