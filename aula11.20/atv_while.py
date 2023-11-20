'''''
while True:
    nota = float(input("informe uma nota de 0 a 10: " ))
    if nota <0 or nota >10:
        print("esta nota é inválida")
    else:
        break

while True:
      usuario = str(input("informe o nome de usúario: "))
      senha = str(input('Informe a senha: '))
      if usuario == senha:
        print("erro, por favor insira as informações novamente")
      else:
          print("login concluído")
          break
'''
