f = str(input('Digite um frase: ')).upper() .strip()
print('A letra A aparece {} vezes na frase'.format(f.count('A')))
print('A primeira letra A apareceu na posisão {}'.format(f.find('A')+1))
print('A ultima letra A apareceu na posisão {}'.format(f.rfind('A')+1))
