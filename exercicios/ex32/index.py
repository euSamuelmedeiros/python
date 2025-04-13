from datetime import date
n = int(input('que ano vc quer analisar? coloque o 0 para analisa o ano atual: '))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('o ano {} é bissexto'.format(n))
else:
    print('o ano {} nao é bissexto'.format(n))