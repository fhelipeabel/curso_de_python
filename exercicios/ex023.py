# Separando dígitos de um número

num = int(input("Digite um número: "))
u = int(num // 1 % 10)
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
#Forma 1
print("\nAnalisando o número: {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

#Forma 2
numero = str(num)

print("\nAnalisando o número: {}".format(num))
print("Unidade: {}".format(numero[3]))
print("Dezena: {}".format(numero[2]))
print("Centena: {}".format(numero[1]))
print("Milhar: {}".format(numero[0]))
