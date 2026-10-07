# Analisando triângulo v1.0

r1 = int(input("Primeiro lado: "))
r2 = int(input("Segundo lado: "))
r3 = int(input("Terceiro lado: "))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("O triângulo pode \33[1;32mSIM\33[m ser formado.")
else:
    print("O triângulo \33[1;31mNÃO\33[m pode ser formado.")