# Ano bissexto
# Método mais iniciante e complicado
ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("\33[1;34mAno bissexto\33[m (exceção rara dos 400 anos)")
        else:
            print("\33[1;31mAno não bissexto\33[m (por regra de ano % 100 != 0)")
    else:
        print("\33[1;34mAno bissexto\33[m")
else:
    print("\33[1;31mAno não bissexto\33[m (por regra do módulo de ano / 4 != 0)")
