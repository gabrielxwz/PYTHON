'''
teste.txt
arq.txt
teste02.doc

hello_word.py

String

a = "Paulo"

16.10
16.11
16.12
18.10
23.10
23.11
29.10

10.16
10.18
10.23
10.29
11.16
12.16

8599

Regras
1. diretorio padrão sempre em letras maiusculas
2. diretorios secundarios sempre em letras minusculas e com numeração da data invertida.
Ex.: aula10.16
3F. nomes das <tags> sempre em letras minusculas obedecendo a semantica.
3B. nomes de variaveis sempre em letra minuscula sempre obedecendo a convenção snake_case
1. explorer do VSCode. Ou seja explorador de pastas e arquivos
2. search de arquivos e pastas ou a busca.
3. (IMPORTANTE) Ele é o plugin do GIT no VSCode
4. Ambiente de testes unitarios do VSCode
5. Ambiente de extenções e plugins do VSCode

6. Configurações do VSCode

CRUD - Create.Read.Update.Delete
       Criar  Ler  Atualizar Deletar

Lista - Mutavel, Iteravel, Suporta varios tipos de dados, possui indices, aceita metodos e fatiamentos.
Obs.: Lista tem seu proprio CRUD
Metodos: append, insert, del, remove, pop, len, extend, copy
parametro: []

obs: polimorfismos - é a capacidade de alguma coisa ser utilizada de varias formas em varias situações

Tuplas - sua principal caracteristica é ser imutavel
parametro: ()

obs: caso você não informe o parametro da lista[] ou da tupla(), o python transforma o conteudo em uma tupla por conta da imutabilidade.

Atividade:
1. faça um codigo que cria uma lista de 5 números inteiros imprime a lista , remove o numero do meio e imprime a lista atualizada.
2. faça um codigo que cria uma lista de 10 números reais e imprima só os pares e depois só os impares
3. faça um codigo que pede 3 notas de quatro alunos, calcula a media e printa as medias em uma lista.
4. faça um codigo que pede 5 letras e quando for consoante ele avisa "É uma consoante", imprima uma lista com as consolantes encontradas
5. faça um codigo que crie uma lista com 20 números inteiros e armazene os números pares na lista pares e os números impares na lista impar, imprima as duas listas.

itareveis, são objetos que podem sofrer iteração. É uma repetição, ou seja podemos executar um processo ou uma ação repetidas vezes sobre esse objeto e em seus elementos

Set = são conjuntos e esses conjuntos no Python são os mesmos conjuntos que aprendemos na escola

caracteristicas: não tem indice, não garantem ordem de elementos, são iteraveis(for, in, not in), são mutaveis mas só acitam tipos imutaveis dentro dele, não podem conter elementos duplicados

parametro: {}

metodos: add(), update(), clear() e discard()

criando um set: set('Paulo') ou {1, 3, 5, 7}


Estruturas de Repetição
while e o for

while - observar a possibilidade de não repetições
for - observar a possibilidade de repetições

contador
while condição:
    codigo
    implementar o contador

break = quebra as estruturas de repetição

for contador:
   codigo

Peça a idade de 20 alunos. Faça um codigo que avisa quando o aluno tem mais de 13 anos.

faça um codigo que peça uma nota, entre zero e dez. Se a nota for menor que 0 e maior que 10 saia do codigo

Loop Infinito - quando uma estrutura de repetição não tem fim

faça um codigo que peça uma nota, entre zero e dez. Mostre uma mensagem caso a nota seja inválida e continue pedindo até que o usuário informe uma nota válida.

faça um codigo que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e pedindo as informações novamente.

faça um codigo que leia 5 números e informe o maior número.

For - é uma estrutura de repetição, um ponto a ser observado é que o "for' ele deve ser utilizado em casos que você sabe a quantidade de repetições.

na grande maioria das vezes você vai utilizar o metodo RANGE() para montar a chamada do "for"

range(i, f, s) - i = INICIO, f = FIM, s = STEP(salto)
Obs: voc~e não é obrigado a passar os três valores do range. Caso passe apenas um valor ser considerado como valor do FIM.

range(5)
range(1, 5)

Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.