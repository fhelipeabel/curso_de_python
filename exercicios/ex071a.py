# Simulador de caixa eletrônico

restante = None

valor_saque = int(input("Qual valor você deseja sacar? "))

duzentos = valor_saque // 200
sobra_dos_duzentos = valor_saque % 200

cem = sobra_dos_duzentos // 100
sobra_dos_cem = sobra_dos_duzentos % 100

cinquenta = sobra_dos_cem // 50
sobra_dos_cinquenta = sobra_dos_cem % 50

vinte = sobra_dos_cinquenta // 20
sobra_dos_vinte = sobra_dos_cinquenta % 20

dez = sobra_dos_vinte // 10
sobra_dos_dez = sobra_dos_vinte % 10

cinco = sobra_dos_dez // 5
sobra_dos_cinco = sobra_dos_dez % 5

dois = sobra_dos_cinco // 2
sobra_dos_dois = sobra_dos_cinco % 2

if duzentos > 0:
    print(f"Total de {duzentos} cédulas de R$ 200,00")
if cem > 0:
    print(f"Total de {cem} cédulas de R$ 100,00")
if cinquenta > 0:
    print(f"Total de {cinquenta} cédulas de R$ 50,00")
if vinte > 0:
    print(f"Total de {vinte} cédulas de R$ 20,00")
if dez > 0:
    print(f"Total de {dez} cédulas de R$ 10,00")
if cinco > 0:
    print(f"Total de {cinco} cédulas de R$ 5,00")
if dois > 0:
    print(f"Total de {dois} cédulas de R$ 2,00")
if sobra_dos_dois > 0:
    print(f"Só será possível sacar R$ {valor_saque - sobra_dos_dois:.2f} e sobrará R$ {sobra_dos_dois:.2f}")