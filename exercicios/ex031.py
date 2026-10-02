# Custo da viagem

dist = int(input("Qual será a distância da viagem em km? "))

if dist >= 200:
    c = 0.45
else:
    c = 0.5

print("Como o percurso será de {}Km, o custo por KM é {} e você precisa pagar no total R$ {}.".format(dist, c, dist*c))