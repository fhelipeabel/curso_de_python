# Super Progressão Aritmética v3.0
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
cont = 1
termo = primeiro
escolha = 1
print(termo, end=" → ")
while cont < 10:
    termo += razao
    cont += 1
    print(termo, end= " → ")
print("FIM")

while escolha != 0:
    escolha = int(input("Mais quantos termos você deseja que eu mostre? "))
    for i in range(0, escolha):
        termo += razao
        cont += 1
        print(termo, end= " → ")
print("FIM")