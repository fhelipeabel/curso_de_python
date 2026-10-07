# Escreva um programa que leia um valor em metros e exiba ele convertido em centímetros e milímetros
metro = int(input("Digite o valor em metros: "))
centímetro = metro * 100
milímetro = centímetro * 10

print("\33[1;33m{}\33[mm, equivale a \33[1;33m{}\33[mcm, que equivale a \33[1;33m{}\33[mmm.".format(metro, centímetro, milímetro))