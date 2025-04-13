# escreva um progama que faça o cumputador 'pensar' em um  numero de o a 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pela maquina.

#o progama deverá escrever na tela sobre quem perdeu ou venceu




from random import randint
from time import sleep
pc = randint(0 , 5)
print('-=-' * 20)
print('vou pensar em algum numero entre 0 e 5. tente adivinhar....')
print('-=-' * 20)
joga = int(input('em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if joga == pc:
    print('BOOOAA, vc venceu!!')
else:
    print('vc perdeu, coloque outra ficha e tente novamente.')