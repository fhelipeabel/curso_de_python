# Super Progressão Aritmética v3.0
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
cont = 1
termo = primeiro
escolha = 10
total = 0

while escolha !=0:
    total += escolha
    while cont <= total:
        print(termo, end=" → ")
        termo += razao
        cont += 1
    print("PAUSA")

    escolha = int(input("Mais quantos termos você deseja que eu mostre? "))

print(f"Progressão finalizada com {total} termos mostrados.")