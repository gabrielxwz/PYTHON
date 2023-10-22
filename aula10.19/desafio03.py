salario = float(input('salario do coladorador: '))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

print('salario original: R$', salario)
print('percentual: ',percentual,'%')

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento

print('aumento: R$ ',aumento)
print('novo salario: R$ ', novo_salario)

