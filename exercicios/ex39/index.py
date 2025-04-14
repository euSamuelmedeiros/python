# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
at = date.today().year
na = int(input('Ano do seu nascimento: '))
id = at - na
print('quem nasceu em {} tem {} anos em {}'.format(na, id, at))
if id == 18:
    print('vc tem que se alistar IMEDIATAMENTW')