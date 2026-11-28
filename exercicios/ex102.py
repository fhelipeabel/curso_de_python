def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número desejado.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o caminho fatorial.
    :return: O resultado do cálculo fatorial de num.
    """
    tot = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        tot *= c
    return tot

# Programa principal
print(fatorial(5, False))
help(fatorial)