# Analisando Triângulos

A = int(input("Lado A: "))
B = int(input("Lado B: "))
C = int(input("Lado C: "))

if A < B + C and B < A + C and C < A + B:
    print("Este triângulo pode \33[32mSIM\33[m ser formado.", end=" ")

    if A == B == C:
        print("Equilátero")
    elif A != B != C != A:
        print("Escaleno")
    else:
        print("Isósceles")

else:
    print("Este triângulo \33[31mNÃO\33[m pode ser formado.")