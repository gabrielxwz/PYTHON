"""
Questão 02

• Escreva um programa que, recebe uma palavra e uma frase, crie uma função que verifique se as letras da palavra aparecem na frase, e quantas vezes aparecem. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: você deve validar se a frase tem pelo menos 25 caracteres

Exemplos do resultado:
    palavra = "pato" 
    frase = "a capa do livro velho"
    P aparece 1 vez
    A aparece 3 vezes
    T não aparece
    O aparece três vezes
"""
def letras_indice(palavra, alfabeto):
    if len(palavra) < 3:
        print("A palavra que ter 3 ou mais letras.")
        return

    for letra in set(palavra):
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            print(f"'{letra}' está no índice {indice} .")


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

palavra = input("Digite uma palavra de no mínimo 3 letras: ").lower()

letras_indice(palavra, alfabeto)