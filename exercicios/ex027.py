# Primeiro e último nome de uma pessoa

nome = input("Digite um nome: ")
nome_sep = nome.split()
first = nome_sep[0]
last = nome_sep[len(nome_sep) - 1]
print("\nO primeiro nome é \33[1;33m{}\33[m".format(first))
print("O último nome é \33[1;33m{}\33[m".format(last))
print("\nO nome resumido é \33[1;33m{}\33[m \33[1;33m{}\33[m".format(first, last))