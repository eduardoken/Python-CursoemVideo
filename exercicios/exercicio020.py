# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho
# dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
from random import shuffle

n1 = str(input('Digite o nomes dos alunos \n1°: '))
n2 = str(input('2°: '))
n3 = str(input('3°: '))
n4 = str(input('4°: '))

lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem sorteada fica em:\n')
for aluno in lista:
    print(aluno)
