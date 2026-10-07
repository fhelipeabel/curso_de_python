import math

num = float(input("Digite um valor: "))
print("O valor digitado foi \33[1;33m{}\33[m e a sua porção inteira é \33[1;33m{}\33[m.".format(num, math.trunc(num)))


# Conclusão: Podemos usar .floor(), .trunc(), e int()