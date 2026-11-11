# Lista ordenada sem repetições
lista = []
for i in range(0, 5):
    n = int(input("Digite um valor: "))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print(f"Adicionado ao final da lista.")
        print(lista)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos}")
                print(lista)
                break
            pos += 1
print(f"\nOs valores digitados em ordem foram {lista}")