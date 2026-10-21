# Sequência de Fibonacci

n = int(input("Digite um número: "))
y = 0
z = 1
i = 0

while i < n:
    print(y, end=" → ")
    print(z, end=" → ")
    y = y + z
    z = z + y
    i += 2

print("FIM")