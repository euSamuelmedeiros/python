s1 = float(input('Qual é o salario do funcionario: R$'))
if s1 < 1250:
    n1 = (s1 * 15 / 100)
    sn = s1 + n1
    print('o funcionario que recebia R${} com o reajuste de salario comecou a receber R${:.2f}'.format(s1 , sn))
else:
    n2 = (s1 * 10 /100)
    sn2 = s1 + n2
    print('o funcionario que ganhava R${} apos o reajuste, passou a ganhar R${:.2f}'.format(s1, sn2))