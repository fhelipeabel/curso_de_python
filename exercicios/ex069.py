# Análise de dados do grupo

maiores_dezoito = homens = mulheres_mais_jovens = 0
seguir = True

while seguir == True:
    print("-"*20)
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    while sexo not in "MF":
        sexo = input("Digite uma opção de sexo válido (M/F): ").strip().upper()
    
    if idade >= 18:
        maiores_dezoito += 1

    if sexo == "M":
        homens += 1
    elif sexo == "F":
        if idade < 20:
            mulheres_mais_jovens += 1

    print("-"*20)
    continuar = input("Você deseja continuar? [S/N]: ").strip().upper()
    if continuar == "N":
        print("\nFinalizando sistema...")
        break

print(f"\nForam registradas {maiores_dezoito} pessoas com mais de 18 anos.")
print(f"{homens} homens foram cadastrados.")
print(f"Qtd de mulheres com menos de 20 anos: {mulheres_mais_jovens}")