def leiaInt(msg):
    ok = False
    while True:
        resp = str(input(msg))
        if resp.isnumeric():
            return int(resp)
            ok = True
        else:
            print("\33[31mERRO! Digite um número inteiro válido.\33[m")

        if ok:
            break


# Programa Principal
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")