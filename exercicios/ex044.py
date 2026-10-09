# Gerenciador de Pagamentos

print("\n{}{}{}".format("="*10, "LOJAS RAMOS", "="*10))
valor_compra = float(input("Total de compras: R$ "))
print("\nFORMAS DE PAGAMENTO")
print("[1] pix/dinheiro/débito")
print("[2] cartão de crédito")
opcao = int(input("\nEscolha uma opção: "))

if opcao == 1:
    print(f"\nVocê ganhou 10% de desconto!\nValor total: R$ {valor_compra * 0.9:.2f}\n")
elif opcao == 2:
    parcelas = input("\nQuantidade de parcelas: ")
    if parcelas == "1":
        print(f"\nÀ vista no cartão você ganhou 5% de desconto.\nValor total: R$ {valor_compra * 0.95:.2f}\n")
    elif parcelas == "2":
        print(f"\nEm duas vezes, consigo fazer sem juros.\nValor total: R$ {valor_compra:.2f}")
    else:
        print(f"\n3 parcelas ou mais, tem taxa de 20%.\nValor total: R$ {valor_compra * 120 / 100:.2f}")