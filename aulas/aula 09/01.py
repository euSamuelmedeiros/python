frase = 'curso em video em python'
#vai verificar o cumprimento da strig
print(len(frase))

#contar quantas vezes o item selecionado aparece na string
print(frase.count('o', 0 , 13))

#vai verificar se tem a palavra selecionada usando o operador (in)
print('curso' in frase)

#transformação
#replace --> trocar vai trocar a frase selecionada
print(frase.replace('python', 'android'))

 # title --> ira analizae quantas palavras tem na string e deixar cada letra de cada palavra em maiuscula
print(frase.title())

# frase.strip --> irá remover todos os espaços inuteis da sa string
print(frase.strip())

#divisao
#criar espaços em espaços vagos na sua string
print(frase.split())

#junção --> join --> juntar strings separadas por (split)
print('-'.join(frase))
 
