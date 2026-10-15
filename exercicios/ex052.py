# Números primos

n = int(input("Digite o número: "))
s = 0

if n < 1:
    print("Digite um número maior do que 0.")

else:
    for c in range(1, n+1):
        if n % c == 0:
            s += 1
            print(f"\33[33m{c}\33[m", end=" ")
        else:
            print(f"\33[31m{c}\33[m", end=" ")
            
if s == 2:
    print(f"\n\33[32mO número {n} é primo\33[m")
else:
    print(f"\nO número \33[31m{n}\33[m não é primo.")