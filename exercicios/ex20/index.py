import random
l1 = str(input('primeiro aluno: '))
l2 = str(input('segundo aluno: '))
l3 = str(input('terceiro aluno: '))
l4 = str(input('quarto aluno: '))
list = [l1 , l2 , l3 , l4]
random.shuffle(list)
print('a ordem de apresentaçao dos trabalho é: ')
print(list)
