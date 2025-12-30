from utilidadesCev import moeda

valor = float(input('Escreve um valor> '))

print (f'\nA metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}\n'
      f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}\n'
      f'Com aumento de 15%: {moeda.moeda(moeda.aumentar(valor))}\n'
      f'Com uma redução de 10%: {moeda.moeda(moeda.diminuir(valor))}')