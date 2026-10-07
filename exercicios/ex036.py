# Aprovando empréstimo

valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário: R$ "))
anos = int(input("Digite os anos de prestação: "))
qtd_parcelas = anos * 12

limite_parcela = salario * 0.3
valor_parcela = valor_casa / qtd_parcelas

print("Para pagar uma casa de R$ {:.2f} em {} anos, precisa ter uma renda mensal de pelo menos R$ {:.2f}.".format(valor_casa, anos, (valor_casa / (anos * 12)) / 3 * 10))

if limite_parcela >= valor_parcela:
    print("O empréstimo foi \33[32maprovado\33[m.")
else:
    print("O empréstimo foi \33[31mnegado\33[m.")