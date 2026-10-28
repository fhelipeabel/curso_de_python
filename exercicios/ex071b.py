# Simulador de caixa eletrônico versão mais certa e menos viajada

cedula = 200
qtd_cedulas = 0

valor_restante = int(input("Digite um valor para sacar: "))
while cedula > 0:
    if valor_restante // cedula == 0:
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 0
            break
    qtd_cedulas = valor_restante // cedula
    valor_restante = valor_restante % cedula
    print(f"Total de {qtd_cedulas} cédulas de R$ {cedula:.2f}")

print(f"Sobrou R$ {valor_restante:.2f}")