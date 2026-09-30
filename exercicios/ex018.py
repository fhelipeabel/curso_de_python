# Seno, Cosseno e Tangente
import math

def calcular(angulo):
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo))
    return ("\nO seno do ângulo {0}° é {1:.2f};\nO cosseno do ângulo {0}° é {2:.2f};\nA tangente do ângulo {0}° é {3:.2f}.".format(int(angulo), seno, cosseno, tangente))

angulo = float(input("Digite o ângulo: "))
print(calcular(angulo))