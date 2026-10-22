# Progressão aritmética (PA)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
cont = 1
termo = primeiro

while cont <= 10:
    print(termo, end=" → ")
    termo += razao
    cont += 1

print("FIM")