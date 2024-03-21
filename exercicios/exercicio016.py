# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc
# import math

n = float(input('Digite um número: '))
print('o número {} tem seu intero {}'.format(n, trunc(n)))
# floor arredonda para baixo então não seria o certo mas funciona
# o certo seria trunc que some com todos os números após o ponto
