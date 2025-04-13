# EStruturas de condicoes

"""n1 = str(input('Qual é o seu nome? '))
if n1 == 'Samuel':
    print('que nome bonito que vc tem')
    print('bom dia {}'.format(n1))
else:
    print('ola, bom dia, {}'.format(n1))
    print('eu nao te conheço')"""

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('digite  sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua media bimestral foi de {:.1f}'.format(m))
if m >= 6.0:
    print('a sua media esta em um padrao bom. parabens  ')
else: 
    print('sua media nao esta muito boa, estude mais.')


