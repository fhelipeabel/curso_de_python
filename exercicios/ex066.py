# Vários números com flag

s = q = n = 0

while n != 999:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    q += 1

print(f"Foram digitados {q} números.")
print(f"A soma dos números vale {s}.")