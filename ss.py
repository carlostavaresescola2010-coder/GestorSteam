# C&T online

saldo = 315
carrinho = []

print("===Bem Vindo a C&T===")
print(" Como é sua primeira vez no C&T seu saldo é:", saldo)

cupom = input("Tem cupom de desconto? s/n: ")
desconto = 0

if cupom == "s":
    codigo = input("Digite o código de cupom: ")
    if codigo == "DESC10":
        desconto = 10
        print("Cupom Válido, 10% desconto!!!")
    elif codigo == "DESC20":
        desconto = 20
        print("Cupom Válido, 20% desconto!!!")
    else:x
        print("Cupom Inválido")


def menu():
    print("1-Camisa 23€")
    print("2-Calças 40€")
    print("3-Sapato 110€")
    print("4-Chapéu 15€")
    print("5-Conjuntos 290€")
    print("6-Ver carrinho")
    print("7-Ver Saldo")
    print("8-Finalizar e pagar")
    print("9-Sair sem pagar")


option = "0"

while option != "9":
    menu()
    option = input("Qual categoria deseja: ")

    if option == "1":
        preco = 17 - (17 * desconto / 100)
        carrinho.append(("Camisa", preco))
        print("----Camisa adicionada ao carrinho!!!----")

    elif option == "2":
        preco = 20 - (20 * desconto / 100)
        carrinho.append(("Calças", preco))
        print("----Calças adicionada ao carrinho!!----")

    elif option == "3":
        preco = 110 - (110 * desconto / 100)
        carrinho.append(("Sapato", preco))
        print("----Sapato adicionada ao carrinho!!----")

    elif option == "4":
        preco = 15 - (15 * desconto / 100)
        carrinho.append(("Chapéu", preco))
        print("----Chapéu adicionado ao carrinho----")

    elif option == "5":
        preco = 290 - (290 * desconto / 100)
        carrinho.append(("Conjuntos", preco))
        print("----Conjunto adicionado ao acarrinho!!!----")

    elif option == "6":
        print("\nSEU CARRINHO:")
        if len(carrinho) == 0:
            print("Carrinho vazio")
        else:
            total = 0
            for item in carrinho:
                print("-", item[0], "€", item[1])
                total = total + item[1]
            print("\nTotal a pagar:", total , "€")

    elif option == "7":
        print("\n--- SEU SALDO ATUAL ---")
        print("€", saldo)
        print("-----------------------")

    elif option == "8":
        if len(carrinho) == 0:
            print("\nCarrinho vazio! Adicione produtos primeiro.")
        else:
            total = 0
            for item in carrinho:
                total = total + item[1]

            print("\n--- RESUMO DA COMPRA ---")
            for item in carrinho:
                print("-", item[0], "€", item[1])
            print("\nTotal: €", total)

            if saldo >= total:
                saldo = saldo - total
                print("\nPAGAMENTO APROVADO!")
                print("Saldo restante: €", saldo)
                break
            else:
                falta = total - saldo
                print("\nSALDO INSUFICIENTE!")
                print("Faltam €", falta)
                print("Remova alguns itens do carrinho.")

    elif option == "9":
        print("\nVocê saiu sem comprar. Até logo!")
        break