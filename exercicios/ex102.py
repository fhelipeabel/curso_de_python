def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número desejado.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o caminho fatorial.
    :return: O resultado do cálculo fatorial de num.
    """
    tot = 1
    for c in range(num, 0, -1):
        tot *= c
    print()
    if show:
        for c in range(num, 1, -1):
            print(f"{c} x", end=" ")
        print(f"1 = ", end="")
        return tot
    return tot

# Programa principal
print(fatorial(5, True))