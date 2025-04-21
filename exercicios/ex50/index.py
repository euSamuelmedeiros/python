#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0
co = 0
for c in range(1,7):
    n1 = int(input('Digite o {} valor: '.format(c)))
    if n1 % 2 == 0:
       s += n1
       co += 1
print('vc me informou {} valore e a soma entre eles é {}'.format(co, s))