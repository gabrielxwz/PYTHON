sexo = input("qual seu sexo? masculino (M) ou feminino (F)? ")
altura = input("digite sua altura: ")

peso_ideal_m = (72.7 * float(altura)) - 58
peso_ideal_f = (62.1 * float(altura)) - 44.7

if sexo == "M":
    print("teu peso ideal e %.2f: " % peso_ideal_m)
elif sexo == "F":
    print("seu peso ideal e %.2f: " % peso_ideal_f)
else:
    print("sexo invalido!")
