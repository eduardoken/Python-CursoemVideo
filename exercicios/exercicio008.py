# Escreva um programa que leia em metros e o exiba convertido em centímetros e milímetros.
m = int(input('quantos metros deseja converter: '))
print('A distancia escolhido foi de {} m convertido em\n{} km \n{} hm \n{} dam \n{} dm \n{} cm \n{} mm.'.format(m, m/1000, m/100, m/10, m*10, (m*100), m*1000))
