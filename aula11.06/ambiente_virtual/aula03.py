# operadores IN e NOT IN(dentro ou não dentro)

nome = "levi"
print( 'le' in nome )

print("="*20)

seu_nome = input('iforme seu nome!: ')
buscar = input('informe o valor a ser encontrado: ')

if ( buscar in nome):
    print(f'{ buscar } esta contido em {seu_nome}')
else:
    print(f'{ buscar } NÃO esta contido em {seu_nome}')

nao_nome = "joãozinho"
print("au" not in nao_nome)
