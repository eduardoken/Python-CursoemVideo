# Faça um algoritmo que leia o preço de um produto e mostre o novo preço, com 5% de desconto.
p = int(input('Digite o preço do produto: '))
print('O valor do produto foi de {} R$ para {} R$'.format(p, p/20))
# 5% = 5/100 = 20
# (x/100)*5 = x*0,05 x*5/100 = ---x/20---
