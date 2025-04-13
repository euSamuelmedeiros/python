"""n = int(input('Me diga um numero qualquer: '))
res = n % 2
if res == 0:
    print('o numero {} é par'.format(n))
else: 
    print('o numero {} é impar'.format(n))"""


n1 = int(input('Qual a distancia da sua viagem: '))
v1 = (n1 * 0.50)
v2 = (n1 * 0.45)
print('vc esta começando uma viagem de {}km'.format(n1))
if n1 <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(v1))
else:
    print('o valor da sua passagem esa em promoçao, vc pagara R${:.2f} por sua passagem.'.format(v2))