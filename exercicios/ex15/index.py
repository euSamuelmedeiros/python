# escreva um progama que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 Km rodado.

da = int(input('Quantos dias alugados? '))
kp = float(input('km percorridos ? '))
pg  = (da * 60) + (kp * 0.15)
print('O o total do valor a pagar pelo aluguem é {}'.format(pg))

 