# ==============================
# jogo.py
# CRUD da entidade Jogo
# armazenamento em dicionario
# validacoes feitas aqui (nao no main)
# ==============================
from utils import gerar_id_jogo

MODOS_VALIDOS = ["single player", "multiplayer", "ambos"]

jogos = {}

# CREATE
def criar_jogo(nome, modo, idade_minima, tamanho_gb):
    while modo.lower() not in MODOS_VALIDOS:
        print(f"  Modo invalido. Escolha: {', '.join(MODOS_VALIDOS)}")
        modo = input("  Modo: ")

    while True:
        try:
            idade_minima = int(idade_minima)
            break
        except ValueError:
            print("  Idade invalida. Introduz um numero inteiro.")
            idade_minima = input("  Idade minima: ")

    while True:
        try:
            tamanho_gb = float(tamanho_gb)
            break
        except ValueError:
            print("  Tamanho invalido. Introduz um numero.")
            tamanho_gb = input("  Tamanho (GB): ")

    jid = gerar_id_jogo()
    jogos[jid] = {
        "nome": nome,
        "modo": modo.lower(),
        "idade_minima": idade_minima,
        "tamanho_gb": tamanho_gb
    }
    print(f"  Jogo criado com sucesso. ID: {jid}")

# READ - listar todos
def listar_jogos():
    if not jogos:
        print("  Nao existem jogos registados.")
        return
    for jid, dados in jogos.items():
        print(f"  ID: {jid} | Nome: {dados['nome']} | Modo: {dados['modo']} | Idade min.: {dados['idade_minima']}+ | Tamanho: {dados['tamanho_gb']} GB")

# READ - consultar individual
def consultar_jogo(jid):
    if jid not in jogos:
        print("  Jogo nao encontrado.")
        return
    dados = jogos[jid]
    print(f"  ID: {jid}")
    print(f"    Nome:        {dados['nome']}")
    print(f"    Modo:        {dados['modo']}")
    print(f"    Idade min.:  {dados['idade_minima']}+")
    print(f"    Tamanho:     {dados['tamanho_gb']} GB")

# UPDATE
def atualizar_jogo(jid, nome=None, modo=None, idade_minima=None, tamanho_gb=None):
    if jid not in jogos:
        print("  Jogo nao encontrado.")
        return
    if modo:
        while modo.lower() not in MODOS_VALIDOS:
            print(f"  Modo invalido. Escolha: {', '.join(MODOS_VALIDOS)}")
            modo = input("  Novo modo (enter para manter): ")
            if not modo:
                modo = None
                break
    if idade_minima:
        while True:
            try:
                idade_minima = int(idade_minima)
                break
            except ValueError:
                print("  Idade invalida. Introduz um numero inteiro.")
                idade_minima = input("  Nova idade minima (enter para manter): ")
                if not idade_minima:
                    idade_minima = None
                    break
    if tamanho_gb:
        while True:
            try:
                tamanho_gb = float(tamanho_gb)
                break
            except ValueError:
                print("  Tamanho invalido. Introduz um numero.")
                tamanho_gb = input("  Novo tamanho GB (enter para manter): ")
                if not tamanho_gb:
                    tamanho_gb = None
                    break

    if nome:         jogos[jid]["nome"]         = nome
    if modo:         jogos[jid]["modo"]         = modo.lower()
    if idade_minima: jogos[jid]["idade_minima"] = idade_minima
    if tamanho_gb:   jogos[jid]["tamanho_gb"]   = tamanho_gb
    print("  Jogo atualizado com sucesso.")

# DELETE
def remover_jogo(jid):
    if jid not in jogos:
        print("  Jogo nao encontrado.")
        return
    del jogos[jid]
    print("  Jogo removido com sucesso.")