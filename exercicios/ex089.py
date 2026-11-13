# Boletim com listas compostas
ficha = list()
cont = 0
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = input("Quer continuar? [S/N] ").upper()
    if continuar == "N":
        break

print(f"-"*30)
print(f"{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}")
print(f"-"*26)
for pos, aluno in enumerate(ficha):
    print(f"{pos:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")
while True:
    print(f"-"*35)
    qual = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))
    if qual == 999:
        print("Finalizando...")
        break
    if qual <= len(ficha) - 1:
        print(f"Notas de {ficha[qual][0]} são {ficha[qual][1]}")