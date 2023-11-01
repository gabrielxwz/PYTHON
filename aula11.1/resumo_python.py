# resumo sobre python!

# Python trata-se de uma linguagem de programação de uso geral, que pode ser usada para criar grandes variedades
# de aplicações. 

# python se tornou uma das linguagens de programação mais populares do mundo nos ultimos anos
# e utilizado em tudo, desde o aprendizado de maquinas a construção de sites, automação de tarefas e 
# testes de softwere.

# o python inicialmente foi desenvolvido na decada de 1980 pelo programador holandes guido van rossum,
# e teve em 1991 sua primeira versão lançada na holanda.

# o python tem 8 tipos de dados padrão, sendo eles:(int), (float), (complex), (str), (bool), (list), (tuple), (dict).
# o (int) é um tipo usado para um numero qe pode ser escrito sem um componente decimal.
# o (float) é um tipo composto por numeros decimais, usado para numeros racionais.
# o (complex) é usado para representar numeros complexos.
# o (str) ou string é um conjunto de caracteres utilizados para representar palavras, frases ou textos.
# o (bool) ou boleanos é um tipo de dado logico que pode representar apenas dois valores: verdadeiro ou falso.
# o (list) é um conjunto de elementos variados: podendo conter:inteiros, floats, strings, ou outros.
# o (tuple) é um tipo que agrupa um conjunto de elementos.
# o (dict) são utilizados para agrupar elementos atraves de estruturas de chave e valor.

# outra informação muito importante de sabemos são as estruturas condicionais (if) (elif) (else), as estruturas
# condicionais são utilizados para controlar o fluxo de execução de programas.
# o (if) usamos quando pretendemos verificar se umas ação e verdadeira.
# o(else) usamos if e else em conjunto para fazermos uma das ações presentes no codigo sejam execultadas. 
# usamos os 3 juntos quando presisamos verificar mais de uma condição.

# outra coisa importante são as estruturas de repetição
# elas são quando queremos que um bloco de codigos seja executado varias vezes.
# ela tem duas formas (For), (While).
# for:
for i in range(1,10):
    print(i)

# while:
gastos=0
valor_gasto=0
while gastos < 1000:
    valor_gasto = int(input("digite o valor gasto: "))
    gastos = gastos + valor_gasto
print(gastos)