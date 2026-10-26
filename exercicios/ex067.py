# Tabuada v3.0

n = 0

while n >= 0:
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-"*35)
    if n <= 0:
        print("Programa TABUADA encerrado. Volte sempre!")
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {n*c}")
    print("-"*35)