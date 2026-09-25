# Escreva um programa que leia um valor em metros e exiba ele convertido em centímetros e milímetros
metro = int(input("Digite o valor em metros: "))
centímetro = metro * 100
milímetro = centímetro * 10

print("{}m, equivale a {}cm, que equivale a {}mm.".format(metro, centímetro, milímetro))