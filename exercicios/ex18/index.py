import math
an = float(input('angulo desejado: '))
sen = math.sin(math.radians(an))
print('o angulo de {} tem o seno de {:.2f}.'.format(an, sen))
tan = math.tan(math.radians(an))
print('O angulo de {} tema tangente igual a {}'.format(an, tan))
cos = math.cos(math.radians(an))
print('o angulo de {} tem o cosseno de {}'.format(an, cos))
