# Unindo dicionários e listas
pessoas = []
mulheres = []
totage = 0
while True:
    pessoa = {
        "nome": input("Nome: "),
        "sexo": input("Sexo: ").upper(),
        "idade": int(input("Idade: "))
    }
    if pessoa["sexo"] == "F":
        mulheres.append(pessoa["nome"])
    pessoas.append(pessoa)
    totage += pessoa["idade"]
    continuar = str(input("Continuar? [S/N]: ")).upper()
    if continuar == "N":
        break
print("-="*30)
print(f"— O grupo tem {len(pessoas)} pessoas.")
media = totage / len(pessoas)
print(f"— A média de idade é de {media:.1f} anos.")
print(f"— As mulheres cadastradas foram: ",end="")
for m in mulheres:
    print(f"{m}", end=" ")
olders = []
print(f"\n— Lista das pessoas que estão acima da média:")
for pessoa in pessoas:
    if pessoa["idade"] > media:
        print(f"\nNome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]}")
print("<< ENCERRADO >>")