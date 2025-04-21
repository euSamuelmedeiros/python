#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n1 = int(input('Digite um numero: '))
if n1 % 1 and n1 == 0:
    print('o numero {} é um numero primo.'.format(n1))