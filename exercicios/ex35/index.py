print('-=-' * 10)
print('Analisador de triangulos')
print('-=-' * 10)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Sim, é possivel criar um triangulo com esses tres segmentos.')
else:
    print('os segmentod a cima nao podem formar um triangulo')