# Dicionário em Python
aluno = {}
nome = input("Nome: ")
media = float(input(f"Média de {nome}: "))
aluno["Nome"] = nome
aluno["Média"] = media
aluno["Situação"] = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
for k, v in aluno.items():
    print(f"{k} é {v}")