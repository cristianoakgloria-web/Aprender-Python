aluno = {'Nome':str(input('Nome do/a aluno/a> ')), 'Média':float(input('Escreve a média(0 a 20)> '))}

if aluno['Média'] >= 11:
    print(f'{aluno["Nome"]} está aprovado/a com um média de {aluno["Média"]}')

elif 10 <= aluno['Média'] < 11:
    print(f'{aluno["Nome"]} está em recuperação com um média de {aluno["Média"]}')

else:
    print(f'{aluno["Nome"]} está reprovado/a com um média de {aluno["Média"]}')