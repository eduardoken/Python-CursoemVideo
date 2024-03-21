from math import sqrt
import random
import emoji

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {}'.format(num, raiz))


num = random.randint(1, 10)
print('número aleatorio', num)

print(emoji.emojize('eae :OK_hand:'))
