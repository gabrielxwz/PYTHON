# count - função é contar quantas vezes um determinado caractere aparece em uma string.
# power e lower - dois metodos que deixam todas as strings em minúscuculas ou maiúsculas.
# find - busca por uma expressão por dentro da frase.
#replace - é utilizado para realizar alterações dentro das strings.
# capitalize - deixa a ´primeira letra das palavras maiúsculas
# split - transforma sua string em uma lista

frase = " A banana é amarela e o abacate é verde.".lower()
letra = 'e'
email = ' paulo.junior@gmail.com '
print(f'A letra "{ letra }" aparece { frase.count(letra)} vezes na frase" { frase }" .')
achei = frase.find('é')
if achei >= 0:
    print(f'A expressão foi encontrada no indice { achei }')
else:
    print(f'A expressão NÃO foi encontrada')    
'''
saida