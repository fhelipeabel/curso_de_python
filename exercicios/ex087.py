# Mais sobre matriz em Python
matriz = [[],[],[]]
for linha in matriz:
    for cel in range(0, 3):
        linha.append(int(input(f"Digite um valor para [{matriz.index(linha)}, {cel}]: ")))
print("-="*30)
soma_terceira_col = soma_pares = 0
for linha in matriz:
    for cel in linha:
        print(f"[ {cel} ]", end=" ")
        if cel % 2 == 0:
            soma_pares += cel
        if linha.index(cel) == 2:
            soma_terceira_col += cel
    print("")
print("-="*30)
print(f"A soma de todos os valores pares é {soma_pares}.")
print(f"A soma dos valores da terceira coluna é {soma_terceira_col}.")
print(f"O maior valor da segunda linha é {max(matriz[1])}.")
print("-="*30)