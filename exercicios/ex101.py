def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade < 16:
        status_obrig = "NÃO VOTA"
    elif 16 <= idade < 18 or idade >= 65:
        status_obrig = "VOTO OPCIONAL"
    else:
        status_obrig = "VOTO OBRIGATÓRIO"

    return f"Com {idade} anos: {status_obrig}."

# Programa principal
print("-"*30)
ano_nasc = int(input("Em que ano você nasceu? "))
print(voto(ano_nasc))