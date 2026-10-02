# Primeiro e último nome de uma pessoa

nome = input("Digite um nome: ")
nome_sep = nome.split()
first = nome_sep[0]
last = nome_sep[len(nome_sep) - 1]
print("\nO primeiro nome é {}".format(first))
print("O último nome é {}".format(last))
print("\nO nome resumido é {} {}".format(first, last))