# Catetos e hipotenusa
import math

co = int(input("Comprimento do cateto oposto: "))
ca = int(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print("A hipotenusa vale {:.2f}.".format(hi))