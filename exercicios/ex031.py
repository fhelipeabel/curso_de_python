# Custo da viagem

dist = float(input("Qual será a distância da viagem em km? "))

if dist >= 200:
    preço = 0.45
else:
    preço = 0.5

print("Como o percurso será de \33[1;33m{}km\33[m, o custo por KM é \33[1;33m{}\33[m e você precisa pagar no total R$ \33[1;33m{:.2f}\33[m.".format(dist, preço, dist*preço))