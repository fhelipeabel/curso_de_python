# Validando expressões matemáticas
expressao = input("Digite a expressão: ")
pent_list = []
for pent in expressao:
    if pent == "(":
        pent_list.append(pent)
    elif pent == ")":
        if len(pent_list) > 0:
            pent_list.pop()
        else:
            pent_list.append(")")
            break
if len(pent_list) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')