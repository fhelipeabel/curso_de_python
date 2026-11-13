# Lista composta e análise de dados
p = list()
pessoas = list()
maior_peso = menor_peso = 0
mais_pesados = list()
menos_pesados = list()
while True:
    p.append(str(input("Nome: ")))
    p.append(float(input("Peso: ")))
    pessoas.append(p[:])
    p.clear()
    continuar = input("Quer continuar? [S/N]: ").upper()
    if continuar in "N":
        break
for p in pessoas:
    if maior_peso == 0:
        maior_peso = menor_peso = p[1]
    else:
        if p[1] > maior_peso:
            maior_peso = p[1]
        elif p[1] < menor_peso:
            menor_peso = p[1]
for p in pessoas:
    if p[1] == maior_peso:
        mais_pesados.append(p[0])
    elif p[1] == menor_peso:
        menos_pesados.append(p[0])
print(f"\nForam cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maior_peso}Kg. Peso de ", end="")
for p in mais_pesados:
    print(f"[{p}]", end=" ")
print(f"\nO menor peso foi de {menor_peso}Kg. Peso de ", end="")
for p in menos_pesados:
    print(f"[{p}]", end=" ")