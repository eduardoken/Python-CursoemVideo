# Faça um algoritmo que leia o salário de um funário e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite o salário de seu funcionário: '))
print('O salário de seu funcionário foi de {:.2f}R$ para {:.2f}R$.'.format(s, s*15/100+s))
