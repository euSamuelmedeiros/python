#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

from datetime import date
id = int(input("Em que ano vc nasceu: "))
ya = date.today().year
res = ya - id
print('O atleta nasceu em {}'.format(res))
if res <= 9:
    print('classificação MIRIM')
elif res <= 14:
    print('Classificaçao INFANTIL')
elif res <= 19:
    print('Classificação JUNIOR')
elif res <= 25:
    print('Classificação SENIOR')
else:
    print('Classificação MASTER')
