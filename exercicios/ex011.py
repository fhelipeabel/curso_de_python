# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

altura = int(input("Digite a largura da parede: "))
largura = int(input("Digite a altura da parede: "))

area = altura * largura
tinta = 2

print("A área total da parede é de {}.".format(area))
print("Você precisará de {} latas de tinta para pintá-la completamente.".format(area/tinta))