s = 0
co = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        co += co + 1
        s += c
print(' a soma de todos os {} valores solicitados é{}'.format(co,s))        
        
