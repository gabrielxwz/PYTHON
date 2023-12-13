"""
Questão 07

• Crie uma função que gere uma lista com tuplas em seus elementos, nas tuplas devem conter dois valores nome e idade 

Ex.: [('paulo', 28), ('Jose', 23), ('Roberto', 17)] 

Ainda deve fazer:
• excluir o ultimo valor
• adicionar uma nova tupla no inicio da lista
• Crie uma cópia da lista para não utilizar o mesmo endereço de memoria

"""
def lista_tupla():
    lista = []
    num_pessoas = int(input("Digite o número de pessoas que serão adicionadas a lista: "))

    for i in range(num_pessoas):
        nome = input(f'Informe o {i+1}º nome: ')
        idade = int(input(f'Informe a {i+1}ª idade: '))

        lista.append((nome,idade))
    return lista

lista = lista_tupla()
print("lista com tuplas: ")
print(lista)

print("\nexcluir o ultimo valor")
del lista[-1]
print(lista)

print("\nadicionar uma nova tupla no inicio da lista")
nova_tupla = ('alguém', 2000)
lista.insert(0,(nova_tupla))
print(lista)

print("\nCrie uma cópia da lista para não utilizar o mesmo endereço de memoria")
copia_lista = lista.copy()
print(copia_lista)
z