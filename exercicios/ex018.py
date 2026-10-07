# Seno, Cosseno e Tangente
import math

def calcular(angulo):
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo))
    return ("\nO seno do ângulo {0}° é \33[1;33m{1:.2f}\33[m;\nO cosseno do ângulo {0}° é \33[1;33m{2:.2f}\33[m;\nA tangente do ângulo {0}° é \33[1;33m{3:.2f}\33[m.".format(int(angulo), seno, cosseno, tangente))

angulo = float(input("Digite o ângulo: "))
print(calcular(angulo))