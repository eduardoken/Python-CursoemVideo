# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import pow, sqrt
# , hypot
ca = float(input('Digite o largura do cateto adjacente: '))
co = float(input('Digite a altura do cateto oposto: '))
h = sqrt(pow(ca, 2) + pow(co, 2))
print('O comprimento da hipotenusa é', h)
# ca = float(input('Digite o largura do cateto adjacente: '))
# co = float(input('Digite a altura do cateto oposto: '))
# h = (ca ** 2 + co ** 2) ** (1/2)

# h = math.hypot(ca, co)
