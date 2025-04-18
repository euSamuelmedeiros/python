#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
res = (n1 + n2) / 2
print('tirando a nota {:.1} e {:.1f} a media dele sera de {:.1f}'.format(n1, n2, res))
if res >= 5 and res <7:
    print('o aluno esta de RECUPERAÇAO')
elif res > 7:
     print('O aluno está APROVADO')
else:
     print('O aluno esta REPROVADO')
