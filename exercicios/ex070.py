# Estatísticas em produtos

seguir = True
produto_mais_barato = ""
menor_preco = None
total_gasto = maior_de_mil = 0

while seguir:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))

    if menor_preco is None:
        menor_preco = preco
        produto_mais_barato = nome
    else:
        if preco < menor_preco:
            menor_preco = preco
            produto_mais_barato = nome

    if preco >= 1000:
        maior_de_mil += 1

    total_gasto += preco

    continuar = ""
    while continuar not in ["S", "N"]:
        continuar = input("Deseja continuar? [S/N] ").strip().upper()

        if continuar == "N":
            print("\n--- RESUMO DA COMPRA ---")
            seguir = False
            break
        elif continuar == "S":
            break

print(f"Total gasto na compra: R$ {total_gasto:.2f}")
print(f"{maior_de_mil} produtos custaram mais de R$ 1.000,00")
print(f"O produto mais barato é o {produto_mais_barato}")