# Análise de dados em uma Tupla

n1 = int(input("Digite o 1° valor: "))
n2 = int(input("Digite o 2° valor: "))
n3 = int(input("Digite o 3° valor: "))
n4 = int(input("Digite o 4° valor: "))

lista = (n1, n2, n3, n4)
cont_9 = 0
pos_3 = 0
par = 0

for valor in lista:
    if valor % 2 == 0:
        par += 1
    if valor == 9:
        cont_9 += 1
    if valor == 3:
        pos_3 = lista.index(3) + 1

print(f"O número 9 foi digitado {cont_9} vezes." if cont_9 > 0 else "O número 9 não foi digitado em nenhum momento.")
print(f"O número 3 apareceu pela primeira vez na {pos_3} posição." if pos_3 > 0 else "O número 3 não foi digitado em nenhum momento.")
print(f"O total de números pares é {par}")