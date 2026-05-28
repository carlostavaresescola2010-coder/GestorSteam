import random

opcao = "0"

animais = ["gato", "cao", "tartaruga", "peixe", "pombo"]

while opcao != "3":
    print("=== MENU ===")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")<<

< <<   # Jogar
    if opcao == "1":
        animal_secreto = random.choice(animais)
        tentativas = 5

        print("=== JOGO INICIADO< ===")
        print("Estou a pensar num animal.")
        print("Tens 5 tentativas para acertar.")

        # Dicas simples
        if animal_secreto == "gato":
            dica = "Dica: Mia e adora caixas."
        elif animal_secreto == "cao":
            dica = "Dica: Late e abana a cauda."
        elif animal_secreto == "tartaruga":
            dica = "Dica: Anda devagar e tem casco."
        elif animal_secreto == "peixe":
            dica = "Dica: Vive dentro de agua."
        elif animal_secreto == "pombo":
            dica = "Dica: Encontras muito nas cidades."

        print(dica)

        while tentativas > 0:
            chute = input("Qual é o animal? ").lower()

            if chute == animal_secreto:
                print("Parabéns! Acertaste!")
                break
            else:
                tentativas -= 1
                print("Errado! Tentativas restantes:", tentativas)

        if tentativas == 0:
            print("Perdeste! O animal era:", animal_secreto)

    # Regras
    elif opcao == "2":
        print("=== REGRAS ===")
        print("1 - O computador escolhe um animal aleatorio.")
        print("2 - Recebes uma dica para ajudar.")
        print("3 - Tens 5 tentativas para adivinhar.")
        print("4 - Escreve o nome do animal corretamente.")
        print("5 - Boa sorte!")

    # Sair
    elif opcao == "3":
        print("A sair do jogo... Obrigado por jogar!")

    # Opção inválida
    else:
        print("Opção inválida. Escolhe 1, 2 ou 3.")
