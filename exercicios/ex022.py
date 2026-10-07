# Analisador de textos
nome = input("Digite o nome completo: ")
print("\nMaiúsculo: \33[1;33m{}\33[m".format(nome.upper()))
print("Minúsculo: \33[1;33m{}\33[m".format(nome.lower()))
print("Comprimento: \33[1;33m{}\33[m".format(len(nome)))
print("Comprimento sem espaços: \33[1;33m{}\33[m".format(len(nome) - nome.count(" ")))
dividido = nome.split()
print("Comprimento primeiro nome: \33[1;33m{}\33[m".format(len(dividido[0])))