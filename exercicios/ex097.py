# Um print especial
def escreva(txt):
    comprimento = (len(txt)+6)
    print("~"*comprimento)
    print(f"{txt:^{comprimento}}")
    print("~"*comprimento)

nome = input("Nome: ")
escreva(nome)