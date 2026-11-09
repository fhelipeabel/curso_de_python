# Lista ordenada sem repetições

lista = []

for i in range(0, 5):
    n = int(input("Digite um valor: "))
    if len(lista) == 0:
        lista.append(n)
        print(f"Primeiro número adicionado à lista na posição {lista.index(n)}")
        print(lista)
    else:
        if n > max(lista):
            lista.append(n)
            print(f"Adicionado ao final da lista...")
            print(lista)
        elif n < min(lista):
            lista.insert(0, n)
            print(f"Adicionado na posição {lista.index(n)} da lista...")
            print(lista)
        elif min(lista) < n < max(lista):
            for item in lista:
                if n < item:
                    lista.insert(lista.index(item), n)
                    print(f"Adicionado na posição {lista.index(n)} da lista...")
                    print(lista)
                    break

print(f"\nOs valores digitados em ordem foram {lista}")