# Separando dígitos de um número

num = int(input("Digite um número: "))
u = int(num // 1 % 10)
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
#Forma 1
print("\nAnalisando o número: {}".format(num))
print("Unidade: \33[1;33m{}\33[m".format(u))
print("Dezena: \33[1;33m{}\33[m".format(d))
print("Centena: \33[1;33m{}\33[m".format(c))
print("Milhar: \33[1;33m{}\33[m".format(m))

#Forma 2
numero = str(num)

print("\nAnalisando o número: \33[1;34m{}\33[m".format(num))
print("Unidade: \33[1;34m{}\33[m".format(numero[3]))
print("Dezena: \33[1;34m{}\33[m".format(numero[2]))
print("Centena: \33[1;34m{}\33[m".format(numero[1]))
print("Milhar: \33[1;34m{}\33[m".format(numero[0]))
