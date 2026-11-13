pessoas = {"nome": "Fhelipe", "sexo": "M", "idade": 22}
del pessoas["sexo"]
pessoas["nome"] = "Abel"
pessoas["peso"] = 98.5
for k, v in pessoas.items():
    print(f"{k} = {v}")