# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('o número {} tem seu dobro {} seu triplo {} e sua raiz quadrada {:.3f}.'.format(n,d,t,r))
