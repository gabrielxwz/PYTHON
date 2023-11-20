'''
# while = enquanto

# loop infinito
# while True

contador = 0
while contador < 300:
    print (contador)
    contador += 1 # contador = contador + 1

    if contador == 20:
        print("cheguei no 20")

    if contador == 290:
        break
'''
aluno = 1
while aluno <= 20:
    idade_aluno = int(input('qual sua idade?'))
    if idade_aluno > 13:
        print(f'O aluno { idade } tem mais de 13 anos')
aluno += 1