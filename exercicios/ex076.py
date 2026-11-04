# Lista de preços com Tupla

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
nome = 0
preço = 1

print("-"*40)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print("-"*40)
for item in produtos:
    while preço <= len(produtos):
        print(f"Item: {produtos[nome]:.<25} R$ {produtos[preço]:>6}")
        nome += 2
        preço += 2