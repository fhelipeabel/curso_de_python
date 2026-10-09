# Classificando atletas
from datetime import date
ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano

if idade < 9:
    print(f"Com {idade} anos, é Mirim")
elif idade >= 9 and idade < 15:
    print(f"Com {idade} anos, é Infantil")
elif idade > 14 and idade < 18:
    print(f"Com {idade} anos, é Junior")
elif idade > 18 and idade < 21:
    print(f"Com {idade} anos, é Sênior")
else:
    print(f"Com {idade} anos, é Master")