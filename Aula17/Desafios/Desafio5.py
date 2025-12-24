def notas(*notas, show = True):
    """
    Função para mostrar a quantidade, média, maior nota e a menor
    
    :param notas: todas as notas
    :param show: True para mostrar a situação ou False para não mostrar
    """
    quantidade = 0
    média = 0
    maior = 0
    menor = 0
    for nota in notas:
        quantidade += 1
        média += nota
        if maior == 0 or maior < nota:
            maior = nota
        if menor == 0 or menor > nota:
            menor = nota
    média /= quantidade
    resultado = f'─ Quantidade de notas: {quantidade}\n─ A maior nota: {maior}\n─ A menor nota: {menor}\n─ A média da turma: {média}'
    situação = ''

    if show:
        if média > 15:
            situação = '\n─ A situação: Excelente.'
        elif 15 >= média >= 11:
            situação = '\n─ A situação: Boa.'
        elif 11 > média >= 10:
            situação = '\n─ A situação: Mediana.'
        elif 10 > média >= 6:
            situação = '\n─ A situação: Má.' 
        else:
            situação = '\n─ A situação: Péssima.'

    return f'{resultado}{situação}'
print(notas(20, 18, 8, 17, 15))