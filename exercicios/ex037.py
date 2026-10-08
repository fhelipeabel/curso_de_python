# Conversor de bases

n = int(input("Digite o número: "))
b = input("\n1 - Binária\n2 - Octal\n3 - Hexadecimal\n\nPara qual basedecimal você deseja converter? ")

if b == "1":
    print(f"O número {n} convertido para a base binária é {bin(n)}.".format(n, bin(n)))

elif b == "2":
    print(f"O número {n} convertido para a base octal é {oct(n)}.")

elif b == "3":
    print(f"O número {n} convertido para a base hexadecimal é {hex(n)}.")

else:
    print("Opção inválida.")