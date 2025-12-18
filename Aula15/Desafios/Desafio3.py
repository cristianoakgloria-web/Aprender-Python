trabalhador = {'Nome':str(input('Nome> ')),
               'Nascimento':int(input('Ano de nascimento> ')),
                'Contratação':int(input('1º ano de contratação> '))}

print(f'{trabalhador["Nome"]}, tu tens {2025 - trabalhador["Nascimento"]} anos e vais se aposentar com {(2025 - trabalhador["Nascimento"]) + (35 - (2025 - trabalhador["Contratação"]))}')
