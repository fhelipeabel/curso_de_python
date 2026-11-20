def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


while True:
    num = int(input("Digite um número: "))
    if par(num):
        print("É par!")
    else:
        print("Não é par!")