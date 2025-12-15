girabola = ('Petro de Luanda', '1º de Agosto', 'Wiliete', 'Bravos de Maquis','Libolo',
             'Desportivo da Lunda Sul', '1º de Maio de Benguela', 'Kabuscorp',
               'Sagrada Esperança', 'Redonda', 'Académica do Lobito', 'Luanda City',
                 'Desportiva da Huíla', 'Interclube', 'Clube Desportivo São Salvador', 'Guelson')

print('As 5 primeiras equipas: {}\n' \
'As 4 últimas equipas: {}\n' \
'A tabela em ordem alfabetica: {}\n' \
'O Luanda City está na {}º posição.'.format(girabola[:5], girabola[12:], 
                                            sorted(girabola), girabola.index('Luanda City') + 1))