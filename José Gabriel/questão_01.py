"""
Questão 01

• Escreva um programa que, recebe uma palavra, crie uma função que verifica na lista "alfabeto" a que indice pertence cada letra da palavra. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: letras repetidas devem ser verificadas somente uma vez

Exemplos do resultado:
    palavra = "cidade" 
    C está no indice 2
    I está no indice 8
    D está no indice 3
    A está no indice 0
    E está no indice 4
"""
def indice():
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z' ]
    alfabeto_fora_lista = "".join(alfabeto).upper()
    print(alfabeto_fora_lista)
    p  = input("digite uma palavra: ").upper()
    while True:
        l_v = input("digite a a letra da sua palavra que deseja verificar: ").upper()
        if l_v not in p:
            l_v = input("a letra digitada deve estar contida na palavra: ").upper()
        print('a palavra foi "{}";  a letra procurada "{}" esta no indice {} do alfabeto '.format(p, l_v ,alfabeto_fora_lista.find(l_v)))
        saida = int(input("digite 1 para encerrar, continuar digite 2 : "))
        if saida == 1:
            break
        else:
            continue

indice()