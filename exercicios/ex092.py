# Cadastro de trabalhador em Python
from datetime import date
funcionario = {}
funcionario["Nome"] = str(input('Nome: '))
ano_nasc = int(input("Ano de nascimento: "))
funcionario["Idade"] = date.today().year - ano_nasc
funcionario["CTPS"] = int(input('Carteira de trabalho: '))
if funcionario["CTPS"] != 0:
    ano_admissao = int(input("Ano de admissão: "))
    funcionario["Admissao"] = ano_admissao
    funcionario["Salário"] = float(input("Salário: "))
    funcionario["Aposentadoria"] = ano_admissao + 35
    print(f"O funcionário é {funcionario["Nome"]}")
    print(f"{funcionario["Nome"]} tem {funcionario["Idade"]} anos")
    print(f"O número da carteira de trabalho é {funcionario["CTPS"]}")
    print(f"Foi contratado em {funcionario["Admissao"]}")
    print(f"O salário é de R$ {funcionario["Salário"]:.2f}")
    print(f"E {funcionario["Nome"]} irá se aposentar em {ano_admissao + 35}, com {ano_admissao + 35 - ano_nasc} anos")
else:
    del funcionario["CTPS"]
    print(f"O funcionário é {funcionario["Nome"]}")
    print(f"{funcionario["Nome"]} tem {funcionario["Idade"]} anos")