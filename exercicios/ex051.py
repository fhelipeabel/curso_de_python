# Progressão aritmética (PA)

# p = int(input("Partida: "))
# r = int(input("Razão: "))

# dc = p + (10 - 1) * r

# for c in range(p, dc + r, r):
#     print(f"{c}", end=" → ")
# print("ACABOU")

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(f"{c}", end= " → ")

print("FIM")