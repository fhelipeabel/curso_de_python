# Função de contador.
from time import sleep

def contador(s,e,p):
    linha()
    print(f"Contagem de {s} até {e}, de {p} em {p}")
    sleep(1)
    if p == 0:
        p = 1
    if s > e:
        p = -abs(p)
        for i in range(s,e-1,p):
            sleep(0.1)
            print(f"{i}", end=" ", flush=True)
    else:
        for i in range(s,e+1,p):
            sleep(0.1)
            print(f"{i}", end=" ", flush=True)
    sleep(0.05)
    print("FIM!")
    sleep(0.5)
def linha():
    print("-="*20)


contador(1,10,1)
contador(10,0,2)
print("-="*20)
print("Agora é sua vez de personalizar a contagem!")
sta = int(input("Início: "))
end = int(input("Fim: "))
pas = int(input("Passo: "))
contador(sta,end,pas)