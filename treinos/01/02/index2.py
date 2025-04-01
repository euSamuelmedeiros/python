
n1 = float(input('number1: '))
n2 = float(input('numnber2: '))
op = input('opreação (+ , - , * , /):')
if op == '+':
        res = n1 + n2
elif op == '-':
        res = n1 - n2
elif op == '*':
        res = n1 * n2
if n2 != 0:
            print('Erro divisao por zero.')
else:
            print('Erro, operação invalida.')
print('o resultado sentre {} e {} é igual a {}'.format(n1, n2, res))


n1 = float(input('number 1: '))
n2 = float(input('number 2: '))
op = input("ecolha a operação (+, -, *, / ):")
if op == '+':
    resul = n1 + n2
elif op == '-':
    resul = n1 - n2
elif op == '*':
    resul = n1 * n2
elif op == '/':
    if n2 != 0:
        resul = n1 / n2
    else:
        resul = 'erro divisão por 0'
else:
    resul = ' operaçao por zero'
print('o resulrado entre {} e {} é {}'.format(n1, n2, resul))




