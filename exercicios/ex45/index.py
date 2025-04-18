#Crie um programa que faça o computador jogar Jokenpô com voce


from random import randint
from time import sleep
it = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
print('-=-' * 11)
jo = int(input('qual a sua jogada? '))
print('-=-' * 11)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
print('O PC jogou {}'.format(it[pc]))
print('O jogador jogou {}'.format(it[jo]))
print('-=-' * 11)
if pc == 0:  # PC jogou PEDRA
    if jo == 0:
        print('EMPATE')
    elif jo == 1:
        print('JOGADOR VENCEU')
    elif jo == 2:
        print('PC VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')

elif pc == 1:  # PC jogou PAPEL
    if jo == 0:
        print('PC VENCEU')
    elif jo == 1:
        print('EMPATE')
    elif jo == 2:
        print('JOGADOR VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')

elif pc == 2:  # PC jogou TESOURA
    if jo == 0:
        print('JOGADOR VENCEU')
    elif jo == 1:
        print('PC VENCEU')
    elif jo == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')
