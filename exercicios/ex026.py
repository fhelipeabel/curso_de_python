# Primeira e última ocorrência de uma string

frase = str(input("Digite uma frase: ")).upper().strip()
print("\nA letra A aparece \33[1;33m{}\33[m vezes".format(frase.upper().count('A') + frase.upper().count('Á') + frase.upper().count('À') + frase.upper().count('Ã') + frase.upper().count('Â')))

first = frase.find('A') + 1
last = frase.rfind('A') + 1
print("Aparece pela primeira vêz na posição \33[1;33m{}\33[m".format(first))
print("Aparece pela última vez na posição \33[1;33m{}\33[m".format(last))