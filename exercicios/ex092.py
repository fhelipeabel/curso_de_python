# Cadastro de trabalhador em Python
from datetime import date
funcionario = dict()
funcionario["Nome"] = str(input('Nome: '))
ano_nasc = int(input("Ano de nascimento: "))
funcionario["Idade"] = date.today().year - ano_nasc
funcionario["CTPS"] = int(input('Carteira de trabalho: '))
if funcionario["CTPS"] != 0:
    funcionario["Admissao"] = int(input("Ano de admissão: "))
    funcionario["Salário"] = float(input("Salário: "))
    funcionario["Aposentadoria"] = funcionario["Idade"] + ((funcionario["Admissao"] + 35) - date.today().year)
print("-="*30)
for k, v in funcionario.items():
    print(f" - {k} tem o valor {v}")