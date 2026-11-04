# Contando vogais em Tupla

palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")

for p in palavras:
    print(f"\nNa palavra \33[34m{p.upper()}\33[m temos", end=" ")
    for letra in p:
        if "a" in p:
            print("\33[33mA\33[m", end=" ")
        if "e" in p:
            print("\33[33mE\33[m", end=" ")
        if "i" in p:
            print("\33[33mI\33[m", end=" ")
        if "o" in p:
            print("\33[33mO\33[m", end=" ")
        if "u" in p:
            print("\33[33mU\33[m", end=" ")