num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)

while True:
    choose = int(input("Qual valor você deseja remover? "))

    if choose in num:
        num.remove(5)
        print(f"Número {choose} removido")
    else:
        print("Não achei o número 5")
print(num)
print(f"Essa lista tem {len(num)} elementos.")