# Função que calcula área
def área(lar, comp):
    print(f"A área de um terreno de {lar} x {comp} é de {lar * comp}m².")

print("Controle de Terrenos")
print("-"*30)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
área(largura, comprimento)