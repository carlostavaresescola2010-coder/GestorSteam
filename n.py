


import random

opcao = "0"


filmes = {
    "Frosen": {
        "genero": "Drama / Romance",
        "frase": "Let it gooo,let it go(música)",
        "ator": "Elsa"
    },
    "Homem Aranha": {
        "genero": "Ficção Científica / Ação",
        "frase": "Com grandes poderes,vem grandes responsabilidades.",
        "ator": "Tom Holland"
    },
    "Batman": {
        "genero": "Aventura / Mistério",
        "frase": "Ou você morre herói, ou vive o suficiente para se tornar o vilão.",
        "ator": "Christian Bale"
    },
    "Harry Potter": {
        "genero": "Fantasia",
        "frase": "Tu és um feiticeiro, Harry.",
        "ator": "Daniel Radcliffe"
    },
    "Velocidade Furiosa": {
        "genero": "Acao",
        "frase": "Nao ha nada mais forte que a familia.",
        "ator": "Vin Diesel"
    }
}

while opcao != "3":
    print("=== MENU ===")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    # Jogar
    if opcao == "1":
        filme_secreto = random.choice(list(filmes.keys()))
        tentativas = 5

        genero = filmes[filme_secreto]["genero"]
        frase = filmes[filme_secreto]["frase"]
        ator = filmes[filme_secreto]["ator"]

        print("=== JOGO INICIADO ===")
        print("Tenta adivinhar o filme!")
        print("Genero:", genero)
        print("Frase famosa:", frase)
        print("Ator:", ator)
        print("Escreve o nome exatamente igual!")

        while tentativas > 0:
            resposta = input("Qual é o filme? ")

            if resposta == filme_secreto:
                print("Parabéns! Acertaste o filme!")
                break
            else:
                tentativas -= 1
                print("Errado! Tentativas restantes:", tentativas)

        if tentativas == 0:
            print("Perdeste! O filme era:", filme_secreto)

    # Regras
    elif opcao == "2":
        print("=== REGRAS DO JOGO ===")
        print("O computador escolhe um filme famoso.")
        print("Recebes dicas: genero, frase famosa e ator.")
        print("Tens 5 tentativas para adivinhar.")
        print("Tens de escrever o nome EXATAMENTE igual ao original.")

    # Sair
    elif opcao == "3":
        print("A sair do jogo... Obrigado por jogar!")

    # Opção inválida
    else:
        print("Opção inválida. Escolhe 1, 2 ou 3.")
