# Maior e menor da sequencia

pesos = []

for c in range(0, 5):
    peso = int(input("Peso: "))
    pesos.append(peso)

print(f"Maior peso: {max(pesos)} | Menor peso: {min(pesos)}")