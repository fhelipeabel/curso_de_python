# Tuplas com Times de Futebol

tabela = ("Flamengo", "Palmeiras", "Cruzeiro", "Fluminense", "Athletico-PR",
          "Bahia", "Atlético-MG", "Bragantino", "Santos", "São Paulo",
          "Coritiba", "Botafogo", "Vasco", "EC Vitória", "Grêmio",
          "Mirassol", "Corinthians", "Internacional", "Remo", "Chapecoense")

print(f"\n\nOs 4 primeiros colocados são:", end=" | ")
for n, time in enumerate(tabela[:4], 1):
    print(f"{n}º - {time}", end=" | ")

print(f"\n\nOs 4 na zona de rebaixamento são:", end=" | ")
for n, time in enumerate(tabela[16:], 17):
    print(f"{n}º - {time}", end=" | ")

print(f"\n\nTodos os times, em ordem alfabética:")
for n, time in enumerate(sorted(tabela), 1):
    print(f"{n}º - {time}")

for time in tabela:
    if time == "Mirassol":
        print(f"\nO Mirassol está em {tabela.index("Mirassol") + 1}º")