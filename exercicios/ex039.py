# Alistamento militar
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nasc
passou = ano_atual - (ano_nasc + 18)
faltam = ano_nasc + 18 - ano_atual

print(f"Sua idade é: {idade}")

if idade == 18:
    print("Está na hora de se alistar. Aliste-se neste ano e boa sorte!")
elif idade == 17:
    print("Se prepare! No próximo ano você precisará se alistar")
elif idade == 19:
    print("Já passou 1 ano do seu período de alistamento militar.")
elif idade >= 20:
    print(f"O seu período de alistamento foi há {passou} anos.")
else:
    print(f"Você ainda vai precisar se alistar daqui a {faltam} anos.")