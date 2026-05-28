#C&T online

saldo = 315
carrinho = []
option = "0"

print("===Bem Vindo a C&T===")
print(" Como é sua primeira vez aqui seu saldo é:", saldo)

#Cupom
cupom = input("Tem cupom de desconto? s/n")
desconto = 0

if cupom == "s":
    codigo = input("Digite o código de cupom:")
    if codigo == "DES10":
       desconto = 10
       print("Cupom Válido, 10% descontoo!!!")
    elif codigo == "DES20":
            desconto = 20
            print("Cupom Válido, 20% descontoo!!!")
    else:
        print("Cupom Inválio")

def menu():
    print("1-Camisa 23€")
    print("2-Calças 40€")
    print("3-Sapato 110€")
    print("4-Chapéu 15€")
    print("5-Conjuntos 290€")
    print("6-Ver Carrinho")
    print("7-Ver Saldo")
    print("8-Finalizar e pagar")
    print("9-Sair sem pagar")

while option != "5":
    menu()
    option = input("Qual categoria deseja:")


    if option == "1":
        preco = 17 - (17 * desconto / 100)
        carrinho.append("Camisa")
        print("---Camisa adicionada ao carrinho!!!---")


    elif option == "2":
        preco = 20 - (20 * desconto / 100)
        carrinho.append("Calças")
        print("---Calças adicionada ao carrinho!!---")


    elif option == "3":
        preco = 110 - (110 * desconto / 100)
        carrinho.append("Sapato")
        print("---Sapato adicionada ao carrinho!!---")

    elif option == "4":
        preco = 15 - (15 * desconto / 100)
        carrinho.append("---Chapéu adicionado ao carrinho---")

    elif option == "5":
        preco = 290 - (290 * desconto / 100)
        carrinho.append("Conjuntos")
        print("---Conjunto adicionado ao acarrinho!!!---")

    elif option == "6":
        print("/nSeu Carrinho:")
        if len(carrinho) == 0:
            print("Carrinho vazio")
        else:
            total = 0
            for item in carrinho:
                print("-", item[0], "€", item[1])
                total = total + item[1]
            print("\nTotal a pagar: €", total)