# Sorteando uma ordem na lista
import random

lista = ["Fhel", "Mari", "Math", "Kimb"]
random.shuffle(lista)

print("\nA ordem para apresentar os trabalhos será a seguinte:")

for ordem, nome in enumerate(lista, start=1):
    print("{}º: {}".format(ordem, nome))