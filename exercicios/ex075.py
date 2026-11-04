# Análise de dados em uma Tupla

lista = (int(input("Digite o 1° valor: ")),
         int(input("Digite o 2° valor: ")),
         int(input("Digite o 3° valor: ")),
         int(input("Digite o 4° valor: ")))
         
print(f"Você digitou os seguintes valores: {lista}")
print(f"O número 9 foi digitado {lista.count(9)} vezes.")
if 3 in lista:
    print(f"O número 3 apareceu pela primeira vez na {lista.index(3) + 1}ª posição.")
else:
    print("O número 3 não foi digitado em nenhuma posição.")
print(f"Números pares digitados: ", end=" ")
for valor in lista:
    if valor % 2 == 0:
        print(valor, end=" ")