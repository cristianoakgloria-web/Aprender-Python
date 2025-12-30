from utilidadesCev import moeda
v = float(input('Escreve um valor em kwanza> '))

print(f'\nA metade de {v} é {moeda.metade(v)}\n'
      f'O dobro de {v} é {moeda.dobro(v)}\n'
      f'Com aumento de 15%: {moeda.aumentar(v)}\n'
      f'Com uma redução de 10%: {moeda.diminuir(v)}')