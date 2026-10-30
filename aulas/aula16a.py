# Tuplas são imutáveis
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")

for comida in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[comida]} na posição {comida}")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")