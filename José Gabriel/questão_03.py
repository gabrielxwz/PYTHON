"""
Questão 03

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. imprima quantas veze aparece a letra "a" no "texto".
02. imprima qual a posição do primeiro "z".
03. leve o "texto" para uma nova variavel e trocando "aprendizado compartilhado" por "vivencia profissional".

"""
texto = "Somos uma escola de tecnologia de informação que cria pontes entre pessoas, conhecimento e empresas. Ambiente que proporciona conexão, troca de conhecimentos e aprendizado compartilhado entre participantes, instrutores e empresas parceiras."

letra = 'a'
print(f'A letra "{ letra }" aparece { texto.count(letra)} vezes na frase" { texto }" .')

achei = texto.find('z')
if achei >= 0:
    print(f'A expressão foi encontrada no indice { achei }')
else:
    print(f'A expressão NÃO foi encontrada')

nova_frase = texto.replace('aprendizado compartilhado', 'vivência profissional')
print(nova_frase)