# Gestor de Notas


nomes = []
notas = []


while True:
    # Mostrar menu
    print("\n=== GESTOR DE NOTAS ===")
    print("1. Inserir nota")
    print("2. Listar notas")
    print("3. Calcular média")
    print("0. Sair")

    opcao = input("\nOpção: ")

    # Inserir nota
    if opcao == "1":
        nome = input("Nome: ")
        nota = float(input("Nota (0-20): "))

        nomes.append(nome)
        notas.append(nota)
        print("Nota adicionada!")

    #Listar notas
    elif opcao == "2":
        print("\n--- NOTAS ---")
        for i in range(len(nomes)):
            print(f"{i + 1}. {nomes[i]}: {notas[i]}")

    #Calcular média
    elif opcao == "3":
        nome_procura = input("Nome: ")

        # Procurar notas do aluno
        notas_aluno = []
        for i in range(len(nomes)):
            if nomes[i] == nome_procura:
                notas_aluno.append(notas[i])

        # Calcular média
        if len(notas_aluno) > 0:
            media = sum(notas_aluno) / len(notas_aluno)
            print(f"Média: {media:.1f}")
        else:
            print("Aluno não encontrado!")

    # Sair
    elif opcao == "0":
        print("Até breve!")
        break

    else:
        print("Opção inválida!")