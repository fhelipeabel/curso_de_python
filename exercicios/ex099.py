# Função que descobre o maior
def maior(*x):
    maior = None
    for i in x:
        if maior is None or i > maior:
            maior = i
    print("-="*30)
    print("Analisando os valores passados...")
    print(f"Foram informados {len(x)} valores ao todo: ", end="")
    for number in x:
        print(number, end=" ", flush=True)
    print(f".\nO maior valor informado foi o {maior}.")

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)