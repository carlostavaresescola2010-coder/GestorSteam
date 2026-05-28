nomes = []
opcao = "0"

while opcao != "6":
    print("\n" + "=" * 25)
    print("    GESTOR DE NOMES")
    print("=" * 25)
    print("1 - Adicionar Nomes")
    print("2 - Remover Nome")
    print("3 - Listar Nomes")
    print("4 - Procurar Nome")
    print("5 - Criar Sigla (N+S)")
    print("6 - Sair")
    print("=" * 25)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        qtd = input("Quantos nomes? ")
        if qtd.isdigit():
            for i in range(int(qtd)):
                nomes.append(input(f"Nome {i + 1}: "))
            print("✅ Adicionado!")
        else:
            print("⚠️ Digite um número!")

    elif opcao == "2":
        remover = input("Nome a remover: ")
        if remover in nomes:
            nomes.remove(remover)
            print("🗑️ Removido!")
        else:
            print("❌ Não encontrado.")

    elif opcao == "3":
        print("\n--- LISTA ---")
        for n in nomes: print("-", n)

    elif opcao == "4":
        busca = input("Procurar por: ")
        if busca in nomes:
            print("🔍 Encontrado!")
        else:
            print("❓ Não encontrado.")

    elif opcao == "5":
        nome_completo = input("Digite Nome e Sobrenome para a sigla: ")
        partes = nome_completo.split()

        if len(partes) >= 2:
            # Pega primeira letra do primeiro [0] e do último [-1] nome
            sigla = partes[0][0].upper() + partes[-1][0].upper()
            nomes.append(sigla)
            print(f"✅ Sigla '{sigla}' guardada na lista!")
        else:
            print("⚠️ Erro: Precisa de pelo menos dois nomes (ex: Vasco Gama).")

    elif opcao == "6":
        print("A fechar programa...")

    else:
        print("🚫 Opção errada! Escolha de 1 a 6.")
        




