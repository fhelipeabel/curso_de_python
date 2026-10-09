# Clássico exercício da média

n1 = float(input("Nota: "))
n2 = float(input("Nota: "))
media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Reprovado")