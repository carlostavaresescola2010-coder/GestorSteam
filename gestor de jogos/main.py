# ==============================
# main.py
# menu terminal para testar CRUD
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

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print("=" * 45)
    print("        🎮  GESTOR DE STEAM  🎮")
    print("=" * 45)

def tabela_resumo():
    from utilizadores import utilizadores
    from jogos import jogos
    print()
    print("  +----------------------+----------+")
    print("  | Entidade             |  Total   |")
    print("  +----------------------+----------+")
    print(f"  | Utilizadores         | {len(utilizadores):<8} |")
    print(f"  | Jogos                | {len(jogos):<8} |")
    print("  +----------------------+----------+")
    print()

def menu():
    limpar()
    cabecalho()
    tabela_resumo()
    print("  1. Utilizadores")
    print("  2. Jogos")
    print("  0. Sair")
    print("-" * 45)

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

        if opcao == "1":
            while True:
                menu_utilizadores()
                op = input("  Opcao: ")
                print()
                if op == "1":
                    nome       = input("  Nome: ")
                    email      = input("  Email: ")
                    password   = input("  Password: ")
                    nascimento = input("  Data de nascimento (DD/MM/AAAA): ")
                    print()
                    criar_utilizador(nome, email, password, nascimento)
                elif op == "2":
                    print()
                    listar_utilizadores()
                elif op == "3":
                    uid = input("  ID do utilizador: ")
                    print()
                    consultar_utilizador(uid)
                elif op == "4":
                    uid        = input("  ID do utilizador: ")
                    nome       = input("  Novo nome (enter para manter): ")
                    email      = input("  Novo email (enter para manter): ")
                    password   = input("  Nova password (enter para manter): ")
                    nascimento = input("  Nova data DD/MM/AAAA (enter para manter): ")
                    print()
                    atualizar_utilizador(
                        uid,
                        nome       if nome       else None,
                        email      if email      else None,
                        password   if password   else None,
                        nascimento if nascimento else None
                    )
                elif op == "5":
                    uid = input("  ID do utilizador: ")
                    print()
                    remover_utilizador(uid)
                elif op == "0":
                    break
                else:
                    print("  Opcao invalida.")
                input("\n  Pressiona ENTER para continuar...")

        elif opcao == "2":
            while True:
                menu_jogos()
                op = input("  Opcao: ")
                print()
                if op == "1":
                    nome         = input("  Nome do jogo: ")
                    modo         = input("  Modo (single player / multiplayer / ambos): ")
                    idade_minima = input("  Idade minima: ")
                    tamanho_gb   = input("  Tamanho (GB): ")
                    print()
                    criar_jogo(nome, modo, idade_minima, tamanho_gb)
                elif op == "2":
                    print()
                    listar_jogos()
                elif op == "3":
                    jid = input("  ID do jogo: ")
                    print()
                    consultar_jogo(jid)
                elif op == "4":
                    jid          = input("  ID do jogo: ")
                    nome         = input("  Novo nome (enter para manter): ")
                    modo         = input("  Novo modo (enter para manter): ")
                    idade_minima = input("  Nova idade minima (enter para manter): ")
                    tamanho_gb   = input("  Novo tamanho GB (enter para manter): ")
                    print()
                    atualizar_jogo(
                        jid,
                        nome         if nome         else None,
                        modo         if modo         else None,
                        idade_minima if idade_minima else None,
                        tamanho_gb   if tamanho_gb   else None
                    )
                elif op == "5":
                    jid = input("  ID do jogo: ")
                    print()
                    remover_jogo(jid)
                elif op == "0":
                    break
                else:
                    print("  Opcao invalida.")
                input("\n  Pressiona ENTER para continuar...")

        elif opcao == "0":
            limpar()
            cabecalho()
            print("\n  Ate logo! 👋\n")
            break
        else:
            print("  Opcao invalida.")
            input("\n  Pressiona ENTER para continuar...")

if __name__ == "__main__":
    main()