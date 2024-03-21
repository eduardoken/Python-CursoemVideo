# Faça um programa que leia a largura e a altura de uma parede, calcule sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m².
l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a = l * h
print('A área da parede é de {} metros² e a quantidade necessária de tinta é de {} litros'.format(a, a/2))
