# Um professor quer sortear um dos seus alunos para pagar o quadro.
# Faça um programa que o ajude ele, lendo o nome dos 4 alunos e leia o sorteado
from random import choice
n1 = str(input('Digite o nome dos quatros alunos \n 1º: '))
n2 = str(input('2º: '))
n3 = str(input('3º: '))
n4 = str(input('4º: '))
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print('O sorteado da vez foi: {}'.format(sorteado))
"""from random import choices
n1 = str(input('Digite o nome dos quatros alunos \n 1º: '))
n2 = str(input('2º: '))
n3 = str(input('3º: '))
n4 = str(input('4º: '))
lista = [n1, n2, n3, n4]
sorteado = choices(lista, k=1)[0]
print('O sorteado da vez foi: {}'.format(sorteado))"""
