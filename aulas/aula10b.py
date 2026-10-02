n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunta nota: "))
m = (n1 + n2) / 2
print("A sua média foi {}.".format(m))

# Condições compostas
if m >= 6.0:
    print("Sua média foi boa. Parabéns!")
else:
    print("Sua média foi ruim... Estude mais.")

# Condições simplificadas
print("A sua média foi {}.".format(m))
print("Parabéns" if m >= 6 else "Estude mais")