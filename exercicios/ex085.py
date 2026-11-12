# Listas com pares e ímpares,
nums = [[],[]]
for i in range(1, 8):
    n = int(input(f"Digite o {i}º valor: "))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
nums[0].sort()
nums[1].sort()
print(f"A lista de pares é: {nums[0]}.")
print(f"A lista de ímpares é {nums[1]}.")