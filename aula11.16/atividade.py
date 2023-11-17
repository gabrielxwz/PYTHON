nomes = []

for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)
    
vogais = ['a', 'e', 'i', 'o', 'u']
nomes_vogais = []

for nome in nomes:
    if nome[0].lower() in vogais:
        nomes_vogais.append(nome)

print("Nomes que começam com vogal:")
for nome in nomes_vogais:
    print(nome)