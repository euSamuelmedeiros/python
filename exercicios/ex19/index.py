# um professor quer sortear umm dos seus quatros alunos para apagar o quadro. faça um progama que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

import random
l1 = str(input('primeiro aluno: '))
l2 = str(input('segundo aluno: '))
l3 = str(input('terceiro aluno: '))
l4 = str(input('quarto aluno: '))
list = [l1, l2, l3, l4]
esc = random.choice(list)
print('o aluno escolhido foi {}'.format(esc))
