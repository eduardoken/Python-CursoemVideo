""" # Faça um programa que leia um angulo qualquer e mostre na tela seu seno, cosseno e tangente
# desse ângulo
import math
angulo = int(input('Digite o valor do ângulo: '))
# pi rad é igual a 180 graus logo rad = pi /180 para calcular os graus usa rad = (pi /180)* o graus
rad = angulo * math.pi / 180
# seno amarzena = math.sin(0) ///sin(graus radiano)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
# calcula indiretamente sem necessidade dos comprimentos
print('O seno de {0} é {1} \nO cosseno de {0} é {2} \nA tangente de {0} é {3}'.format(angulo, sen, cos, tan)) """

"""import math
ang = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(ang, sen))
cos = math.cos(math.radians(ang))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print(' o ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(ang, tan))"""

from math import radians, sin, cos, tan
ang = float(input('Digite o valor do ângulo: '))
sen = sin(radians(ang))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(ang, sen))
cos = cos(radians(ang))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(ang, cos))
tan = tan(radians(ang))
print(' o ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(ang, tan))
