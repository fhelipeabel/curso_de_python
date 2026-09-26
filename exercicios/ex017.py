# Catetos e hipotenusa
import math

cateto_oposto = int(input("Digite o cateto oposto: "))
cateto_adjacente = int(input("Digite o cateto adjacente: "))

hipotenusa = math.sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))
print("A hipotenusa vale {}.".format(hipotenusa))