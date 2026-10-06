# Aumentos múltiplos

sal = int(input("Digite o salário: "))

if sal >= 2500:
    aumento = 10
else:
    aumento = 15

print("Seu salário de R${} aumentará em {}% e passará a ser R${:.2f}".format(sal, aumento, sal + ((sal * aumento) / 100)))