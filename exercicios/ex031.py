# Custo da viagem

dist = float(input("Qual será a distância da viagem em km? "))

if dist >= 200:
    preço = 0.45
else:
    preço = 0.5

print("Como o percurso será de {}Km, o custo por KM é {} e você precisa pagar no total R$ {:.2f}.".format(dist, preço, dist*preço))