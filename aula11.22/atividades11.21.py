maior = 0
menor = None
while True:
    saida = input('Digite "S" para sair Ou Qualquer Outra Tecla Pra Entrar  ')
    if saida == 's' or saida == 'S':
        print ('Volte Sempre!')
        break
    else:
        print ('Você entrou!')
        print("agora informe abaixo o número")
    numero = int(input('informe um numero inteiro: '))
    if numero > maior:
        maior = numero

    if menor == None or numero < menor:
        menor = numero
