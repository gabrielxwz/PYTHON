'''
lista = [['paulo', 5], ['joao', 7], ['daniel', 9]]
dic = {}
dic.update(lista)
print(dic)
lista2 = [['josé', 2], ['pedro', 3], ['tiago', 1.5], ['adriano', 4]]
dic.update (lista2)
print (dic)

while True:
    lista_carros = []
    marca = input('insira o nome do seu carro: ')
    modelo = input('insira o nome do modelo do seu carro: ')
    lista_carros.append(marca)
    lista_carros.append(modelo)
    carros = {}
    carros.update ([lista_carros])
    print (carros)

lista = ['a']
nome = str(input('insira o seu nome: '))
idade = int(input('insira a sua idade: '))
aniversario = (input('insira a data de aniversário '))
endereco: str(input('insira o endereço completo '))

lista.append(nome)
lista.append(idade)
lista.append(aniversario)

cadastro = {}
cadastro.update ([lista])

print (cadastro)
'''


while True:
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
