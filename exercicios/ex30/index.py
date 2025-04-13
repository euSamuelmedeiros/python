#aqui o usuario msm ira colocar o valor em km
vel = int(input('Qual a velocidade do carro? '))
if vel >= 80:
    print('vc foi multado por alta velocidade, sera cobrado 7.00 por cada km a cima do limite.')
    m = (vel*7)-(80*7)
    print('o valor cobrado da multa sera de {}'.format(m))
else:
    print('boa viagem e digija sempre com responsabilidade e segurança.')

#ouu
#aqui foi tipo um sistema de radar, onde a maquina escolhe o valor em km

from random import randint
from time import sleep
print('seu carro passou pelo radar ...')
sleep(2)
vel = randint(10 , 200)
if vel > 80:
    print('vc estava a {}km/hr e foi multado por alta velocidade. O valor a se pagar sera de {}'.format(vel, (vel*7-(80*7))))
else:
    print('tenha um bom dia e dirija sempre com responsabilidade em segurança.')

