# Escreva um programa que converta uma temperatura digitada em °C e coverta para °F
# °F = (°C x 1.8) + 32
c = float(input('Informe a temperatura em °C: '))
f = (c * 1.8) + 32
h = 9 * c / 5 + 32
print('A temperatura de {}°C é convertida em {}°F'.format(c, f))
print('{}°F'.format(h))
