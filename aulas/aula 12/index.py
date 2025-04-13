#estruturas de controle.... 

#condiçoes aninhadas

n = str(input('Qual é o seu nome? '))
if  n == 'Samuel':
   print('que nome bonito!')
elif n == 'pedro' or n == 'ana' or n == 'maria':
   print('na america do sul seu nome é muito popular')
elif n in 'luiza claudia jessica juliana':
   print('belo nome feminino')
else: 
   print('seu nome pe muito normal')
print('tenha um bom dia {}!'.format(n))