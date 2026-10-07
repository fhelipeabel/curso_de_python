# Sorteando uma ordem na lista
from random import shuffle

lista = ["Fhel", "Mari", "Math", "Kimb"]
shuffle(lista)

print("\nA ordem para apresentar os trabalhos será a seguinte:")

for ordem, nome in enumerate(lista, start=1):
    print("\33[1;33m{}\33[mº: \33[1;33m{}\33[m".format(ordem, nome))