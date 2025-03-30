# ultilizando import (biblilioteca)


import math
n = int(input('digite um numero: '))
rz = math.sqrt(n)
print('a raiz de {} é igual a {:.2f}'.format(n, rz))

#segunda maneira de usa o import (pegando so uma funcionalidade)

from math import sqrt
n = int(input('number: '))
rz = sqrt(n)
print('A raiz de {} é igual a {}'.format(n, rz))

import random
n = random.randint(1, 10)
print(n)

