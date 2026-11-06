nome = str(input("Qual é seu nome? "))

if nome == "Fhelipe":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil.")
else:
    print("Seu nome é bem normal.")

print("Tenha um bom dia, \33[32m{}\33[m!".format(nome))