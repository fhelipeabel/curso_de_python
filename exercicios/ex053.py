texto = str(input("Digite o texto: "))

inverso = texto[::-1].upper().replace(" ", "")

print(f"O texto {texto.replace(" ", "").upper()}, ao contrário fica: {inverso}")

if texto.upper().replace(" ", "") == inverso:
    print("Este texto é um palíndromo!")
else:
    print("Não é...")