# Criando um menu de opções

n = ""

print("[1] somar")
print("[2] multiplicar")
print("[3] maior")
print("[4] novos números")
print("[5] sair do programa") 

while n != 5:
    n = int(input("Escolha uma opção: "))
    primeiro = int("Primeiro valor: ")
    segundo = int("Segundo valor: ")

    if n == 1:
        print(f"A soma de {primeiro} com {segundo} dá {primeiro + segundo}")

    elif n == 2:
        print(f"O número {primeiro} x {segundo} dá {primeiro * segundo}")

    elif n == 3:
        if primeiro > segundo:
            print(f"O maior número entre {primeiro} e {segundo} é o {primeiro}")
        elif primeiro < segundo:
            print(f"O maior número entre {primeiro} e {segundo} é o {segundo}")
        else:
            print(f"Não existe um número maior, pois ambos são o mesmo.")

    elif n == 4:
        primeiro = int(input("Digite o novo primeiro valor: "))
        segundo = int(input("Digite o novo segundo valor: "))