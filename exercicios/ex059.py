# Criando um menu de opções

from time import sleep

primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
n = 0

print("\n[1] somar")
print("[2] multiplicar")
print("[3] maior")
print("[4] novos números")
print("[5] sair do programa\n") 

while n != 5:
    n = int(input("\nEscolha uma opção: "))
    if 6 > n > 0:

        if n == 1:
            print(f"A soma de  {primeiro} com {segundo} dá {primeiro + segundo}")

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
            primeiro = int(input("Primeiro valor: "))
            segundo = int(input("Segundo valor: "))

        elif n == 5:
            print("Finalizando o sistema...")
            sleep(1)
            break

    else:
        print("Digite um número entre 1 a 5.")