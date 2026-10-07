# Par ou ímpar

n = int(input("Digite o número: "))

if n % 2 == 0:
    print("O número digitado é \33[1;33mPAR\33[m.")
else:
    print("O número digitado é \33[1;33mÍMPAR\33[m.")