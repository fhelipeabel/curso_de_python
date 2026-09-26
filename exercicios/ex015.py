km = float(input("Quantos KM foram percorridos? "))
t = int(input("Por quantos dias você ficou com o carro? "))

valor_km = km * 0.15
valor_t = t * 60

print("O aluguel total ficou em R$ {:.2f}.".format(valor_km + valor_t))