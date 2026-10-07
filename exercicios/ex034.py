# Aumentos múltiplos

sal = int(input("Digite o salário: "))

if sal >= 2500:
    aumento = 10
else:
    aumento = 15

print("Seu salário de \33[1;33mR${}\33[m aumentará em \33[1;33m{}%\33[m e passará a ser \33[1;33mR${:.2f}\33[m".format(sal, aumento, sal + ((sal * aumento) / 100)))