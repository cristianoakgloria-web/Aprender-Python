palavras = 'Carro', 'Ana','Livro', 'Nietzsche'

for c in range(0, len(palavras)):
    print(f'\nAs vogais da palavra {palavras[c]} são:', end=' ')

    palavra = palavras[c].lower()

    for a in range(0, len(palavra)):
      if (palavra[a]) in 'a' or palavra[a] in 'e' or palavra[a] in 'i' or palavra[a] in 'o' or palavra[a] in 'u':
            print(palavra[a], end = ' ')
print()
