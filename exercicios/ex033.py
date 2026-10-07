# Maior e menor valores

n1 = int(input("Digite o primeiro: "))
n2 = int(input("Digite o segundo: "))
n3 = int(input("Digite o terceiro: "))

lista = [n1, n2, n3]

print("O maior número é \33[1;33m{}\33[m e o menor é o \33[1;33m{}\33[m.".format(max(lista), min(lista)))