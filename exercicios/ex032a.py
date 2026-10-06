# Ano bissexto
# Método mais iniciante e complicado
ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Ano bissexto (exceção rara dos 400 anos)")
        else:
            print("Ano não bissexto (por regra de ano % 100 != 0)")
    else:
        print("Ano bissexto")
else:
    print("Ano não bissexto (por regra do módulo de ano / 4 != 0)")
