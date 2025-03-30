import math
n1 = float(input('cateto oposto: '))
n2 = float(input('cateto adjacente: '))
h = math.hypot(n1, n2)
print('a hipotenusa vai medir {:.2f}'.format(h))