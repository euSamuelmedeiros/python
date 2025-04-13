# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n1 = int(input('Digite um numero inteiro qualquer: '))
print(''' escolha um opção para a conversão
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')
op = int(input('sua opção: '))
if op == 1:
    print('{} convertido para binario é igual a {}'.format(n1, bin(n1)[2]))
elif op == 2:
    print('{} convertido para octal é  igual a {}'.format(n1, oct(n1)[2]))
elif op == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n1, hex(n1)[2]))
else: 
    print('opção invalida, tente novamente')

