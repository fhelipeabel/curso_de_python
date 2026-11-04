# Contando vogais em Tupla

palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")

for p in palavras:
    print(f"\nNa palavra \33[34m{p.upper()}\33[m temos", end=" ")
    for letra in p:
        if letra.upper() in "AEIOU":
            print(f"\33[33m{letra.upper()}\33[m", end=" ")