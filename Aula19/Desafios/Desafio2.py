import requests
try:
    rede = requests.get('https://www.jornaldeangola.ao')
    print('Acessado o site com sucesso! :)')
except:
    print(f'Não é possível acessar o site no momento! :(')