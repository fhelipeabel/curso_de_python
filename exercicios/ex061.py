# Progressão aritmética (PA)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
cont = 1
termo = primeiro

print(termo, end=" → ")

while cont < 10:
    termo += razao
    cont += 1
    print(termo, end= " → ")

print("FIM")