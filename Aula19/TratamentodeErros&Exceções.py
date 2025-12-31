try:
    a = 'n'
    b = 0
    c = a/b
except Exception as erro:
    print(f'Infelizmente tivemos um problema! :(\nERRO: {erro.__cause__}')
except (ValueError, TypeError):
    print('Tivemos um erro com o tipo de dados fornecidos!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferio não informar o número!')
else: 
    print(f'{a} / {b} = {c}')
finally:
    print('FIM.')