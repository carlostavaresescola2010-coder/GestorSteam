# ==============================
# main.py
# menu terminal para testar CRUD
# ponto de entrada do programa
# verifica os codigos de retorno
# e mostra mensagens ao utilizador
# os inputs e loops ficam todos aqui
# ==============================
import os
from utilizadores import (
    criar_utilizador,
    listar_utilizadores,
    consultar_utilizador,
    atualizar_utilizador,
    remover_utilizador
)
from jogos import (
    criar_jogo,
    listar_jogos,
    consultar_jogo,
    atualizar_jogo,
    remover_jogo
)
from loja import (
    criar_item_loja,
    listar_loja,
    consultar_item_loja,
    atualizar_item_loja,
    remover_item_loja
)
from compra import (
    criar_compra,
    listar_compras,
    consultar_compra,
    atualizar_compra,
    remover_compra
)

# limpa o ecra conforme o sistema operativo (Windows ou Linux/Mac)
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# imprime o cabecalho do programa
def cabecalho():
    print("=" * 45)
    print("        🎮  GESTOR DE STEAM  🎮")
    print("=" * 45)

# menu principal
def menu():
    limpar()
    cabecalho()
    print()
    print("  1. Utilizadores")
    print("  2. Jogos")
    print("  3. Loja")
    print("  4. Compras")
    print("  0. Sair")
    print("-" * 45)

# submenu de utilizadores
def menu_utilizadores():
    limpar()
    cabecalho()
    print("\n  ── UTILIZADORES ──\n")
    print("  1. Criar utilizador")
    print("  2. Listar utilizadores")
    print("  3. Consultar utilizador")
    print("  4. Atualizar utilizador")
    print("  5. Remover utilizador")
    print("  0. Voltar")
    print("-" * 45)

# submenu de jogos
def menu_jogos():
    limpar()
    cabecalho()
    print("\n  ── JOGOS ──\n")
    print("  1. Criar jogo")
    print("  2. Listar jogos")
    print("  3. Consultar jogo")
    print("  4. Atualizar jogo")
    print("  5. Remover jogo")
    print("  0. Voltar")
    print("-" * 45)

# submenu da loja
def menu_loja():
    limpar()
    cabecalho()
    print("\n  ── LOJA ──\n")
    print("  1. Adicionar jogo a loja")
    print("  2. Listar loja")
    print("  3. Consultar item da loja")
    print("  4. Atualizar item da loja")
    print("  5. Remover item da loja")
    print("  0. Voltar")
    print("-" * 45)

# submenu de compras
def menu_compras():
    limpar()
    cabecalho()
    print("\n  ── COMPRAS ──\n")
    print("  1. Registar compra")
    print("  2. Listar compras")
    print("  3. Consultar compra")
    print("  4. Atualizar compra")
    print("  5. Remover compra")
    print("  0. Voltar")
    print("-" * 45)

def main():
    while True:
        menu()
        opcao = input("  Opcao: ")

        # ── UTILIZADORES ──────────────────────────────────────────────────────
        if opcao == "1":
            while True:
                menu_utilizadores()
                op = input("  Opcao: ")
                print()

                if op == "1":
                    # recolhe os dados — loop repete se houver erro de validacao (400)
                    while True:
                        nome       = input("  Nome: ")
                        username   = input("  Username: ")
                        email      = input("  Email: ")
                        password   = input("  Password: ")
                        nascimento = input("  Data de nascimento (DD-MM-AAAA): ")
                        print()
                        code, obj = criar_utilizador(nome, username, email, password, nascimento)
                        if code == 201:
                            print(f"  [{code}] Utilizador criado com sucesso. Nome: {obj['nome']}")
                            break
                        elif code == 400:
                            print(f"  [{code}] {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "2":
                    print()
                    code, obj = listar_utilizadores()
                    if code == 200:
                        for uid, dados in obj.items():
                            print(
                                f"  ID: {uid} | Nome: {dados['nome']} | Username: {dados['username']} | Email: {dados['email']} | Nascimento: {dados['nascimento']}")
                    elif code == 404:
                        print(f"  [{code}]  Not Found: {obj}")
                    elif code == 500:
                        print(f"  [{code}] Internal Error: {obj}")

                elif op == "3":
                    # loop repete se o ID nao existir (404)
                    while True:
                        uid = input("  ID do utilizador: ")
                        print()
                        code, dados = consultar_utilizador(uid)
                        if code == 200:
                            print(f"  ID: {uid}")
                            print(f"    Nome:       {dados['nome']}")
                            print(f"    Username:   {dados['username']}")
                            print(f"    Email:      {dados['email']}")
                            # mostra a password mascarada com asteriscos por seguranca
                            print(f"    Password:   {'*' * len(dados['password'])}")
                            print(f"    Nascimento: {dados['nascimento']}")
                            break
                        elif code == 404:
                            print(f"  [{code}]  Not Found: {dados}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {dados}")
                            break

                elif op == "4":
                    # loop repete se o ID nao existir (404) ou dados invalidos (400)
                    while True:
                        uid        = input("  ID do utilizador: ")
                        nome       = input("  Novo nome (enter para manter): ")
                        username   = input("  Novo username (enter para manter): ")
                        email      = input("  Novo email (enter para manter): ")
                        password   = input("  Nova password (enter para manter): ")
                        nascimento = input("  Nova data DD-MM-AAAA (enter para manter): ")
                        print()
                        # passa None nos campos que ficaram em branco
                        code, obj = atualizar_utilizador(
                            uid,
                            nome       if nome       else None,
                            username   if username   else None,
                            email      if email      else None,
                            password   if password   else None,
                            nascimento if nascimento else None
                        )
                        if code == 200:
                            print(f"  [{code}] {obj}")
                            break
                        elif code in (400, 404):
                            print(f"  [{code}] {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "5":
                    # loop repete se o ID nao existir (404)
                    while True:
                        uid = input("  ID do utilizador: ")
                        print()
                        code, obj = remover_utilizador(uid)
                        if code == 200:
                            print(f"  [{code}] {obj}")
                            break
                        elif code == 404:
                            print(f"  [{code}] Not Found: {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "0":
                    break

                else:
                    print("  Opcao invalida.")

                input("\n  Pressiona ENTER para continuar...")

        # ── JOGOS ─────────────────────────────────────────────────────────────
        elif opcao == "2":
            while True:
                menu_jogos()
                op = input("  Opcao: ")
                print()

                if op == "1":
                    # loop repete se houver erro de validacao (400)
                    while True:
                        nome         = input("  Nome do jogo: ")
                        modo         = input("  Modo (single player / multiplayer / ambos): ")
                        idade_minima = input("  Idade minima: ")
                        tamanho_gb   = input("  Tamanho (GB): ")
                        print()
                        code, obj = criar_jogo(nome, modo, idade_minima, tamanho_gb)
                        if code == 201:
                            print(f"  [{code}] {obj}")
                            break
                        elif code == 400:
                            print(f"  [{code}] {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "2":
                    print()
                    code, obj = listar_jogos()
                    if code == 200:
                        print(f"  [{code}] {obj}")
                    elif code == 404:
                        print(f"  [{code}] Not Found: {obj}")
                    elif code == 500:
                        print(f"  [{code}] Internal Error: {obj}")

                elif op == "3":
                    # loop repete se o ID nao existir (404)
                    while True:
                        jid = input("  ID do jogo: ")
                        print()
                        code, obj = consultar_jogo(jid)
                        if code == 200:
                            print(f"  ID: {jid}")
                            print(f"    Nome:        {obj['nome']}")
                            print(f"    Modo:        {obj['modo']}")
                            print(f"    Idade min.:  {obj['idade_minima']}+")
                            print(f"    Tamanho:     {obj['tamanho_gb']} GB")
                            break
                        elif code == 404:
                            print(f"  [{code}] Not Found: {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "4":
                    # loop repete se o ID nao existir (404) ou dados invalidos (400)
                    while True:
                        jid          = input("  ID do jogo: ")
                        nome         = input("  Novo nome (enter para manter): ")
                        modo         = input("  Novo modo (enter para manter): ")
                        idade_minima = input("  Nova idade minima (enter para manter): ")
                        tamanho_gb   = input("  Novo tamanho GB (enter para manter): ")
                        print()
                        # passa None nos campos que ficaram em branco
                        code, obj = atualizar_jogo(
                            jid,
                            nome         if nome         else None,
                            modo         if modo         else None,
                            idade_minima if idade_minima else None,
                            tamanho_gb   if tamanho_gb   else None
                        )
                        if code == 200:
                            print(f"  [{code}] {obj}")
                            break
                        elif code in (400, 404):
                            print(f"  [{code}] {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "5":
                    # loop repete se o ID nao existir (404)
                    while True:
                        jid = input("  ID do jogo: ")
                        print()
                        code, obj = remover_jogo(jid)
                        if code == 200:
                            print(f"  [{code}] {obj}")
                            break
                        elif code == 404:
                            print(f"  [{code}] Not Found: {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "0":
                    break

                else:
                    print("  Opcao invalida.")

                input("\n  Pressiona ENTER para continuar...")

        # ── LOJA ──────────────────────────────────────────────────────────────
        elif opcao == "3":
            while True:
                menu_loja()
                op = input("  Opcao: ")
                print()

                if op == "1":
                    # loop repete se houver erro de validacao (400) ou jogo nao encontrado (404)
                    while True:
                        jid   = input("  ID do jogo: ")
                        preco = input("  Preco (€): ")
                        stock = input("  Stock: ")
                        print()
                        code, obj = criar_item_loja(jid, preco, stock)
                        if code == 201:
                            print(f"  [{code}] Item adicionado a loja com sucesso. ID: {obj}")
                            break
                        elif code in (400, 404):
                            print(f"  [{code}] {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "2":
                    print()
                    code, obj = listar_loja()
                    if code == 200:
                        print(f"  [{code}] {obj}")
                    elif code == 404:
                        print(f"  [{code}] Not Found: {obj}")
                    elif code == 500:
                        print(f"  [{code}] Internal Error: {obj}")

                elif op == "3":
                    # loop repete se o ID nao existir (404)
                    while True:
                        lid = input("  ID do item da loja: ")
                        print()
                        code, obj = consultar_item_loja(lid)
                        if code == 200:
                            from jogos import jogos
                            nome_jogo = jogos[obj["jid"]]["nome"] if obj["jid"] in jogos else "Jogo removido"
                            print(f"  ID: {lid}")
                            print(f"    Jogo:   {nome_jogo} ({obj['jid']})")
                            print(f"    Preco:  {obj['preco']:.2f}€")
                            print(f"    Stock:  {obj['stock']}")
                            break
                        elif code == 404:
                            print(f"  [{code}] Not Found: {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "4":
                    # loop repete se o ID nao existir (404) ou dados invalidos (400)
                    while True:
                        lid   = input("  ID do item da loja: ")
                        preco = input("  Novo preco (enter para manter): ")
                        stock = input("  Novo stock (enter para manter): ")
                        print()
                        # passa None nos campos que ficaram em branco
                        code, obj = atualizar_item_loja(
                            lid,
                            preco if preco else None,
                            stock if stock else None
                        )
                        if code == 200:
                            print(f"  [{code}] {obj}")
                            break
                        elif code in (400, 404):
                            print(f"  [{code}] {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "5":
                    # loop repete se o ID nao existir (404)
                    while True:
                        lid = input("  ID do item da loja: ")
                        print()
                        code, obj = remover_item_loja(lid)
                        if code == 200:
                            print(f"  [{code}] {obj}")
                            break
                        elif code == 404:
                            print(f"  [{code}] Not Found: {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "0":
                    break

                else:
                    print("  Opcao invalida.")

                input("\n  Pressiona ENTER para continuar...")

        # ── COMPRAS ───────────────────────────────────────────────────────────
        elif opcao == "4":
            while True:
                menu_compras()
                op = input("  Opcao: ")
                print()

                if op == "1":
                    # loop repete se houver erro de validacao (400) ou IDs nao encontrados (404)
                    while True:
                        uid         = input("  ID do utilizador: ")
                        lid         = input("  ID do item da loja: ")
                        data_compra = input("  Data de compra (DD-MM-AAAA): ")
                        print()
                        code, obj = criar_compra(uid, lid, data_compra)
                        if code == 201:
                            print(f"  [{code}] Compra registada com sucesso. ID: {obj}")
                            break
                        elif code in (400, 404):
                            print(f"  [{code}] {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "2":
                    print()
                    code, obj = listar_compras()
                    if code == 200:
                        for cid, dados in obj.items():
                            f"  ID: {cid} | Data: {dados['data_compra']} | Preco pago: {dados['preco_pago']:.2f}€"
                        print(f"  [{code}] {obj}")
                    elif code == 404:
                        print(f"  [{code}] Not Found: {obj}")
                    elif code == 500:
                        print(f"  [{code}] Internal Error: {obj}")

                elif op == "3":
                    # loop repete se o ID nao existir (404)
                    while True:
                        cid = input("  ID da compra: ")
                        print()
                        code, obj = consultar_compra(cid)
                        if code == 200:
                            print(f"  ID: {cid}")
                            print(f"    Utilizador:  {obj['username']} ({obj['uid']})")
                            print(f"    Item loja:   {obj['lid']}")
                            print(f"    Data:        {obj['data_compra']}")
                            print(f"    Preco pago:  {obj['preco_pago']:.2f}€")
                            break
                        elif code == 404:
                            print(f"  [{code}] Not Found: {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "4":
                    # so a data e editavel — uid, lid e preco sao imutaveis
                    while True:
                        cid         = input("  ID da compra: ")
                        data_compra = input("  Nova data DD-MM-AAAA (enter para manter): ")
                        print()
                        code, obj = atualizar_compra(
                            cid,
                            data_compra if data_compra else None
                        )
                        if code == 200:
                            print(f"  [{code}] {obj}")
                            break
                        elif code in (400, 404):
                            print(f"  [{code}] {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "5":
                    # loop repete se o ID nao existir (404)
                    while True:
                        cid = input("  ID da compra: ")
                        print()
                        code, obj = remover_compra(cid)
                        if code == 200:
                            print(f"  [{code}] {obj}")
                            break
                        elif code == 404:
                            print(f"  [{code}] Not Found: {obj}")
                        elif code == 500:
                            print(f"  [{code}] Internal Error: {obj}")
                            break

                elif op == "0":
                    break

                else:
                    print("  Opcao invalida.")

                input("\n  Pressiona ENTER para continuar...")

        # ── SAIR ──────────────────────────────────────────────────────────────
        elif opcao == "0":
            limpar()
            cabecalho()
            print("\n  Ate logo! 👋\n")
            break

        else:
            print("  Opcao invalida.")
            input("\n  Pressiona ENTER para continuar...")

# ponto de entrada - so executa main() se este ficheiro for corrido diretamente
if __name__ == "__main__":
    main()