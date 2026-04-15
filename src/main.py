# ==============================
#           MAIN
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
                        nascimento = input("  Data de nascimento (DD/MM/AAAA): ")
                        print()
                        return_code = criar_utilizador(nome, username, email, password, nascimento)
                        if return_code[0] == 201:
                            print(f"  [{return_code[0]}] Utilizador criado com sucesso. ID: {return_code[1]}")
                            break
                        elif return_code[0] == 400:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                        elif return_code[0] == 500:
                            print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")
                            break

                elif op == "2":
                    print()
                    return_code = listar_utilizadores()
                    if return_code[0] == 200:
                        print(f"  [{return_code[0]}] {return_code[1]}")
                    elif return_code[0] == 404:
                        print(f"  [{return_code[0]}] {return_code[1]}")
                    elif return_code[0] == 500:
                        print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")

                elif op == "3":
                    # loop repete se o ID nao existir (404)
                    while True:
                        uid = input("  ID do utilizador: ")
                        print()
                        return_code = consultar_utilizador(uid)
                        if return_code[0] == 200:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                            break
                        elif return_code[0] == 404:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                        elif return_code[0] == 500:
                            print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")
                            break

                elif op == "4":
                    # loop repete se o ID nao existir (404) ou dados invalidos (400)
                    while True:
                        uid        = input("  ID do utilizador: ")
                        nome       = input("  Novo nome (enter para manter): ")
                        username   = input("  Novo username (enter para manter): ")
                        email      = input("  Novo email (enter para manter): ")
                        password   = input("  Nova password (enter para manter): ")
                        nascimento = input("  Nova data DD/MM/AAAA (enter para manter): ")
                        print()
                        # passa None nos campos que ficaram em branco
                        return_code = atualizar_utilizador(
                            uid,
                            nome       if nome       else None,
                            username   if username   else None,
                            email      if email      else None,
                            password   if password   else None,
                            nascimento if nascimento else None
                        )
                        if return_code[0] == 200:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                            break
                        elif return_code[0] in (400, 404):
                            print(f"  [{return_code[0]}] {return_code[1]}")
                        elif return_code[0] == 500:
                            print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")
                            break

                elif op == "5":
                    # loop repete se o ID nao existir (404)
                    while True:
                        uid = input("  ID do utilizador: ")
                        print()
                        return_code = remover_utilizador(uid)
                        if return_code[0] == 200:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                            break
                        elif return_code[0] == 404:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                        elif return_code[0] == 500:
                            print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")
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
                        return_code = criar_jogo(nome, modo, idade_minima, tamanho_gb)
                        if return_code[0] == 201:
                            print(f"  [{return_code[0]}] Jogo criado com sucesso. ID: {return_code[1]}")
                            break
                        elif return_code[0] == 400:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                        elif return_code[0] == 500:
                            print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")
                            break

                elif op == "2":
                    print()
                    return_code = listar_jogos()
                    if return_code[0] == 200:
                        print(f"  [{return_code[0]}] {return_code[1]}")
                    elif return_code[0] == 404:
                        print(f"  [{return_code[0]}] {return_code[1]}")
                    elif return_code[0] == 500:
                        print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")

                elif op == "3":
                    # loop repete se o ID nao existir (404)
                    while True:
                        jid = input("  ID do jogo: ")
                        print()
                        return_code = consultar_jogo(jid)
                        if return_code[0] == 200:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                            break
                        elif return_code[0] == 404:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                        elif return_code[0] == 500:
                            print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")
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
                        return_code = atualizar_jogo(
                            jid,
                            nome         if nome         else None,
                            modo         if modo         else None,
                            idade_minima if idade_minima else None,
                            tamanho_gb   if tamanho_gb   else None
                        )
                        if return_code[0] == 200:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                            break
                        elif return_code[0] in (400, 404):
                            print(f"  [{return_code[0]}] {return_code[1]}")
                        elif return_code[0] == 500:
                            print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")
                            break

                elif op == "5":
                    # loop repete se o ID nao existir (404)
                    while True:
                        jid = input("  ID do jogo: ")
                        print()
                        return_code = remover_jogo(jid)
                        if return_code[0] == 200:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                            break
                        elif return_code[0] == 404:
                            print(f"  [{return_code[0]}] {return_code[1]}")
                        elif return_code[0] == 500:
                            print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")
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
