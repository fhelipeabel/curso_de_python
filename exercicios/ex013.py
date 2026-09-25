# Faça um algorítmo que leia o salário do funcionário e mostre o seu novo salário, mas agora com 15% de aumento.

salario = float(input("Digite seu antigo salário: "))
aumento = float(input("Digite quantos % aumentou: "))

novo_salario = salario * (100 + aumento) / 100

print("Seu novo salário é de R$ {}. Parabéns pelo aumento!".format(novo_salario))