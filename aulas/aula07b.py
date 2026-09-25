n1 = int(input("Digite um número: "))
n2 = int(input("Agora outro: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
md = n1 % n2
print("A soma é {}, o produto é {} e a divisão é {:.3f}.".format(s, m, d), end=" >>> ")
print("A potência é {}, o dividendo inteiro é {} e o módulo é {}.".format(e, di, md))