logins = {  'Usuário1': 'User01', 'Senha': '1234',
            'Usuário2': 'User02',  'Senha': '4321'}

usuario = str(input('digite o nome de usuario: '))
senha = str(input('digite a sua senha: '))

if usuario == 'user01' and senha == '1234':
    print('login validado!')

elif usuario == 'user02' and senha == '4321':
    print('login validado!')

else:
    print('nome de usuário ou senha incorreto')

ver_logins = (input('digite V para ver os logins ou qualquer outra tecla para sair: '))
if ver_logins == 'V' or ver_logins == 'v':
        print('login')
else:
        print("Volte Sempre!")
        break
