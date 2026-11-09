# Validando expressões matemáticas

pent_list = []
expressao = input("Digite a expressão: ")

for c in expressao:
    if c == "(":
        pent_list.append(c)
    elif c == ")":
        if len(pent_list) > 0:
            pent_list.pop()
        else:
            pent_list.append(")")
            break

if len(pent_list) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')