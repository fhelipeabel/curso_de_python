# Seno, Cosseno e Tangente

import math

def calcular(angulo):
    radiano = math.radians(angulo)
    seno = math.sin(radiano)
    cosseno = math.cos(radiano)
    tangente = math.tan(radiano)
    return ("\nO seno do ângulo {0}° é {1:.2f};\nO cosseno do ângulo {0}° é {2:.2f};\nA tangente do ângulo {0}° é {3:.2f}.".format(int(angulo), seno, cosseno, tangente))

angulo = float(input("Digite o ângulo: "))
print(calcular(angulo))