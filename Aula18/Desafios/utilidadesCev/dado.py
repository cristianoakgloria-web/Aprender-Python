import re
def leiaDinheiro(v):
    vv = v.replace(' ', '')
    if vv.find('AOA') == 0 and vv.count('AOA') == 1:
        if re.fullmatch(r'^[0-9]+([,.]?[0-9]+)?$', vv.replace('AOA', '')):
            return v
        else:
            return 'FORMATO INVÁLIDO!'
    else:
        return 'FORMATO INVÁLIDO!'