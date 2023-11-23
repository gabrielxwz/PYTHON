# "for" trabalha com iteráveis
# tem que possuir uma váriavel de controle
# métodos == iter () | next () 

from re import A, L, U


nome = "Paulo"

print (nome[3])
texto = iter(nome)
print (next(texto))
print (next(texto))
print (next(texto))
print (next(texto))

for letra in nome:
    print(letra)
print()



















print ("segunda, terça, quarta, quinta, sexta, sábado, domingo.