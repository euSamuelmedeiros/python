#O ESTUDO VAI TE LEVAR MUITO LONGE
n1 = int(input('informe um numero: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('analisando o numero {}'.format(n1))
print('unidade:{} '.format(u))
print('Dezena:{} '.format(d))
print('Centena:{}'.format(c))
print('millhar:{}'.format(m))