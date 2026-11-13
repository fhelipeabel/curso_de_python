# Matriz em Python
matriz = [[],[],[]]
for linha in matriz:
    for cel in range(0, 3):
        linha.append(int(input(f"Digite um valor para [{matriz.index(linha)}, {cel}]: ")))

for linha in matriz:
    for cel in linha:
        print(f"[{cel:^5}]", end=" ")
    print()