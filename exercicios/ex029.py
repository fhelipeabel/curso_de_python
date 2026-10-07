# Radar eletrônico

vel = int(input("Digite a velocidade: "))

if vel > 80:
    multa = (vel - 80) * 7
    print("Você passou \33[1;33m{}\33[m Km/h acima do permitido.\nPortanto, foi multado em R$ \33[1;33m{:.2f}\33[m".format(vel - 80, multa))

else:
    print("Você passou dentro do limite de velocidade permitido.")