#nome = input('qual é o seu nome?')
#print('prazer em te conhecer {:^10}!'.format(nome))

n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {} o produto é {} e a divisão é {:.3f}'.format(s, m, d)) 
print('a divisão inteira {} e potencia {}'.format(di, e))