# Progressão aritmética

p = int(input("Partida: "))
r = int(input("Razão: "))

dc = p + (10 - 1) * r

for c in range(p, dc + r, r):
    print(f"{c}", end=" → ")
print("ACABOU")