# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
from time import sleep

notas = []

print("Olá! Vamos calcular as suas notas! (Digite 0 para parar)")
while True:
    nota = int(input("Nota: "))
    if nota == 0:
        print("Calculando...")
        sleep(2)
        break
    else:
        notas.append(nota)

media = sum(notas) / len(notas)
print("A sua média das notas é \33[1;33m{}\33[m.".format(media))

# Fiz melhor e ainda coloquei um while True, para ao invés de pedir apenas duas notas, pedir quantas o aluno quiser escrever, com um parâmetro de parada que é o "0".