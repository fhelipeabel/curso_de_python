# Validação de dados

sexo = ""

while sexo != 'M' and sexo != 'F':
    sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print("Digite corretamente.")

print(f"Sexo {sexo} reconhecido.")