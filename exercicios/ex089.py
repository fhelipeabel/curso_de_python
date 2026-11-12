# Boletim com listas compostas
ficha = list()
cont = 0
while True:
    ficha.append([])
    ficha[cont].append(str(input("Nome: ")))
    ficha[cont].append([])
    ficha[cont][1].append(float(input("Nota 1: ")))
    ficha[cont][1].append(float(input("Nota 2: ")))
    print(ficha)
    cont+=1

    continuar = input("Quer continuar? [S/N] ").upper()
    if continuar == "N":
        break

print(f"-"*20)
print("Nº", end="  ")
print("NOME", end=" ")
print(f"{"MÉDIA":^15}")
print(f"-"*20)
for pos, aluno in enumerate(ficha, 1):
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f"{pos}   {aluno[0]:<10}{media:.2f}")
print(f"-"*20)
qual = input("Mostrar as notas de qual aluno? (999 interrompe): ")
