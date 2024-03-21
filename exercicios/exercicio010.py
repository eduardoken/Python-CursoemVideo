# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# considere: US$1 = R$3,27
d = int(input('Escreva sua quantia em dinheiro: '))
print('Você possui {}R$ e pode converte-los em {:.3f}US$.'.format(d, d/3.27))

