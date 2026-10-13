# Números primos

n = int(input("Digite o número: "))
s = 0

for c in range(2, n):
    if n % c == 0:
        s += 1

if s == 0:
    print(f"O número {n} \33[32mé primo.\33[m")
else:
    print(f"O número {n} \33[31mnão é primo\33[m.")