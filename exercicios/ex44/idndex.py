# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros#

print('{:=^40}'.format('LOJAS SAMUCA'))
p = float(input('preço das compra: R$'))
print("""FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartâo""")
op = int(input('Qual é a sua opçao? ' ))
if op == 1:
    con1 = (p * 10 ) / 100
    con2 = p - con1
    print('O valor a ser pago da sua compra será de {:.2f}'.format(con2))
elif op == 2:
    cart1 = (p * 5) / 100
    cart2 = p - cart1
    print('O valor a ser pago da sua compra será de {:.2f}'.format(cart2))
elif op == 3:
    par1 = (p / 2)
    print('sua compra parcelada em 2x dera uma fatura de {:.2f} por mes.'.format(par1))
elif op == 4:
    mai3 = (p * 20) / 100
    res = (p + mai3) / 3 
    print('Sua compra foi parcelada em 3x o valor da fatura dera de {:.2f}'.format(res))
else:
    print('opção invalida')