nm = str(input('digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu noome em maiuculas é {}'.format(nm.upper()))
print('seu nome em minusculas é {}'.format(nm.lower()))
print('Seu nome tem {} caracteres'.format(len(nm)))
#print(' Seu primeiro nome tem {} letras'.format(nm.find(' ')))
sp = nm.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(sp[0], len(sp[0])))



