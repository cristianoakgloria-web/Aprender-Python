from math import sin, cos, tan, radians
ang = float(input('Escreve o número para ângulo> '))
angulo = radians(ang)
print('O seno de {} é {}\n'
      'O cosseno de {} é {}\n'
      'A tangente de {} é {}'.format(ang, sin(angulo),
                                     ang, cos(angulo),
                                     ang, tan(angulo)))