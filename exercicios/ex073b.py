# Tuplas com Times de Futebol

tabela = ("Flamengo", "Palmeiras", "Cruzeiro", "Fluminense", "Athletico-PR",
          "Bahia", "Atlético-MG", "Bragantino", "Santos", "São Paulo",
          "Coritiba", "Botafogo", "Vasco", "EC Vitória", "Grêmio",
          "Mirassol", "Corinthians", "Internacional", "Remo", "Chapecoense")

print(f"\nOs 4 primeiros colocados são: {tabela[:4]}")
print(f"\nOs 4 na zona de rebaixamento são: {tabela[-4:]}")
print(f"\nTodos os times, em ordem alfabética: {sorted(tabela)}")
print(f"\nO Mirassol está em {tabela.index("Mirassol") + 1}º")