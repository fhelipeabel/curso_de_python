# Analisador de textos
nome = input("Digite o nome completo: ")
print("\nMaiúsculo: {}".format(nome.upper()))
print("Minúsculo: {}".format(nome.lower()))
print("Comprimento: {}".format(len(nome)))
print("Comprimento sem espaços: {}".format(len(nome) - nome.count(" ")))
dividido = nome.split()
print("Comprimento primeiro nome: {}".format(len(dividido[0])))