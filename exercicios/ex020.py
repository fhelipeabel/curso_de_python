# Sorteando uma ordem na lista
from random import shuffle

lista = ["Fhel", "Mari", "Math", "Kimb"]
shuffle(lista)

print("\nA ordem para apresentar os trabalhos será a seguinte:")

for ordem, nome in enumerate(lista, start=1):
    print("{}º: {}".format(ordem, nome))