# Analisador completo

nome_masculino = []
idade_masculina = []
sexo_masculino = []

nome_feminino = []
idade_feminina = []
sexo_feminino = []

nomes = []
idades = []
sexos = []

c = 0
qtd_meninas = 0

for i in range(0, 4):
    nome = input(f"\n{i + 1}º Nome: ")
    idade = int(input(f"{i + 1}ª Idade: "))
    sexo = input(f"{i + 1}º Sexo: ")
    i += 1

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

    if sexo == "M":
        nome_masculino.append(nome)
        idade_masculina.append(idade)
        sexo_masculino.append(sexo)

    elif sexo == "F":
        nome_feminino.append(nome)
        idade_feminina.append(idade)
        sexo_feminino.append(sexo)

        if idade < 20:
            qtd_meninas += 1

    else:
        print("Valor 'sexo' inválido. Tente novamente.")
        break

homem_oldest = idade_masculina.index(max(idade_masculina))

print(f"A média da idade do grupo é de {sum(idades) / len(idades):.0f} anos.")
print(f"O homem mais velho é o {nome_masculino[homem_oldest]}.")
print(f"O total de mulheres com menos de 20 anos é {qtd_meninas}.")