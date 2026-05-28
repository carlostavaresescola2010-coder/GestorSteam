import random

opcao = "0"

while opcao != "3":
    print("=== MENU ===")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        numero_secreto = random.randint(1, 50)
        tentativas = 5

        print("=== JOGO INICIADO ===")
        print("Estou a pensar num número entre 1 e 20.")
        print("Tens 5 tentativas.")

        while tentativas > 0:
            chute = int(input("Digite o seu palpite: "))

            if chute == numero_secreto:
                print("Parabéns! Acertaste o número!")
                break
            else:
                tentativas -= 1

                if chute < numero_secreto:
                    print("O número é MAIOR!")
                else:
                    print("O número é MENOR!")

                print("Tentativas restantes:", tentativas)

        if tentativas == 0:
            print("Fim de jogo! O número era:", numero_secreto)

    elif opcao == "2":
        print("=== REGRAS DO JOGO ===")
        print("1 - O computador escolhe um número entre 1 e 20.")
        print("2 - Tens 5 tentativas para adivinhar.")
        print("3 - O jogo diz se o número é maior ou menor.")
        print("4 - Se errares 5 vezes, perdes.")
        print("5 - Volta ao menu para jogar de novo.")

    elif opcao == "3":
        print("A sair do jogo... Obrigado por jogar!")
    else:
        print("Opção inválida. Tenta novamente.")
