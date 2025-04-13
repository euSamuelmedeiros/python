#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 < n2:
    print('o SEGUNDO numero é maior')
elif n1 > n2:
    print('O PRIMEIRO numero é maior')
else:
    print('nao há diferença, ambos sao iguais')