entrada = input('[E] para entra e [S] para passar: ')
senha_digitada = input ('Digite a senha de acesso: ')
senha = "1234567"

if (entrada == 'E' or entrada == 'e'):
    if (senha == senha_digitada):
        print("Sucesso, voce entrou no sistema!!")
    else:
        print("senha incorreta!")
elif (entrada == 'S' or entrada == 's'):
    print("voce escolheu PASSAR!!")
else:
    print("voce não selecionou uma opção valida!")