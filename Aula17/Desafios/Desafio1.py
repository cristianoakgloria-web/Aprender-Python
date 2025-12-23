def votar(ano_nascimento=0):
    """
    Lê o ano de nascimento de uma pessoa e determina se o seu voto é válido, inválido ou opcional. 

    :param ano_nascimento: ano que a pessoa nasceu.
    """
    if (2026 - ano_nascimento) < 18:
        return 'Voto Negado!'
    elif 65 > (2026 - ano_nascimento) >= 18:
        return 'Voto Obrigatório!'
    else:
        return 'Voto Opcional.'
    
n = int(input('Escreve o ano do teu nascimento> '))
print(votar(n))