# Verificando as primeiras letras de um texto

#Jeito que eu fiz
c = input("Digite o nome da cidade: ")
s = c.split()
print(len(s))
if s[0].lower() == "santo" or s[0].lower() == "santa":
    result = True
else:
    result = False

print(result)
if result is False:
    print("\nEsta cidade não começa com 'Santo' ou 'Santa'.")
else:
    print("\nEsta cidade começa sim com 'Santo' ou 'Santa'.")
    

#Jeito que o Guanabara fez
c = input("Digite o nome da cidade: ")
s = c.split()
print(len(s))
print(c[0:5].upper() == 'SANTO')