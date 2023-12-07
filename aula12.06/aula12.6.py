'''
dic = { 'nome': 'paulo'} #Created
dic2 = dict(idade=23) #Created

dic['nome'] #Readed
reading = dic2.get ('idade') #readed

print(dic)
print(dic2)

dic.update(sobrenome = 'junior') #Updated/ inserindo dados
dic.update({'idade': 23})
tupla = ('peso', 72.12),
lista = ['data', '13//04/1996'], ['numeros', [ 1, 2, 3, 4, 5, 6, 8, 9]]
dic.update(tupla)
dic.update(lista)

print (dic)

dic.clear( ) #deleted
print(f'dados do dicionario{dic}')
''''