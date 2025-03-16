a = input('digite algo: ')
print('O tipo primitivo desse valor é:', type(a)) #string
print('só tem espaços?', a.isspace())
print('O resultado é um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('È alfanumerico', a.isalnum())
print('esta em maiusculas?', a.isupper())
print('Esta capitalizada', a.istitle())

n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
soma = int(n1) + int(n2)
res = print('a soma entre {} e {} vale {}'.format(n1, n2, soma))

 