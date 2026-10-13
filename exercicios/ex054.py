# Grupo da maioridade

maior = 0
menor = 0

from datetime import date

for c in range(0, 7):
    y = int(input("Ano de Nascimento: "))
    idade = date.today().year - y
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"Existem {maior} pessoas que já são maiores de idade\ne {menor} pessoas ainda menores.")