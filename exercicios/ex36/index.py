# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

va = float(input('Qual o valor da casa: R$'))
sa = float(input('qual o salario do comprador: R$'))
tp = int(input('em quantos anos pretende pagar a casa? '))
pres = va / (tp * 12)
m = sa * 30 / 100
print('para pagar uma casa de {:.2f} em {} anos'.format(va, tp))
print('a prestaçao será de R${:.2f}'.format(pres))
if pres <= m:
    print('o emprestimo pode ser concedido')
else:
    print('emprestimo negado')