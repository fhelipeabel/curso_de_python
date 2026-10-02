# Radar eletrônico

vel = int(input("Digite a velocidade: "))

if vel > 80:
    multa = (vel - 80) * 7
    print("Você passou {} Km/h acima do permitido.\nPortanto, foi multado em R$ {:.2f}".format(vel - 80, multa))

else:
    print("Você passou dentro do limite de velocidade permitido.")