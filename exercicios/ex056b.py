# Analisador completo 2

maior_idade = 0
qtd_mulheres_jovens = 0
soma_idade = 0


for c in range(1, 5):
    nome = input(f"\nDigite o {c}º nome: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    sexo = input(f"Agora o sexo (F/M) de {nome}: ")

    soma_idade += idade

    if sexo.upper() == "M": 
        if idade > maior_idade:
            maior_idade = idade
            homem_mais_velho = nome

    if sexo.upper() == "F":
        if idade < 20:
            qtd_mulheres_jovens += 1


print(f"\nA média de idade do grupo é {soma_idade / 4:.0f} anos.")
print(f"O homem mais velho é o {homem_mais_velho}, com {maior_idade} anos.")
print(f"O total de mulheres com menos de 20 anos é {qtd_mulheres_jovens}.")