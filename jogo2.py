import random

opcao = "0"

animal=("cão","gato","leão","vaca","rinoceronte")

while opcao != "3":
    print("=== MENU ===")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")


if opcao == "1":
   animal_secreto = random.choice(animal)
   tentativas = 5

  print("===Jogo Iniciado===")
  print("Estou a pensar num animal")
  print("Tens 3 tentativas")

 if animal == "cão":
            dica = "Dica: Late e abana a cauda."
        elif animal == "gato":
            dica = "Dica: Mia e não gosta de tomar banho."
        elif animal  == "leão":
            dica = "Dica: É um predador e rei da selva."
        elif animal == "vaca":
            dica = "Dica: Da leite e come ervas."
        elif animal == "rinoceronte":
            dica = "Dica: É grande e tem chifre em cima do nariz ."

        print(dica)

        while tentativas > 0:
            chute = input("Qual é o animal? ").lower()

            if chute == animal:
                print("Parabéns! Acertaste!")
                break
            else:
                tentativas -= 1
                print("Errado! Tentativas restantes:", tentativas)

        if tentativas == 0:
            print("Perdeste! O animal era:", animal)

              elif opcao == "2":
                   print("===Regras===")
                   print("1 - O computador escolhe um animal aleatório")
                    print("2 - Tens 3 tentativas para adivinhar.")