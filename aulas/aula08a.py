from math import sqrt, floor

num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raíz de {} é igual a {}.".format(num, floor(raiz)))
print("Mas o número real é {}.\n".format(raiz))