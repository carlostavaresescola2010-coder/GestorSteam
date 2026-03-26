# ==============================
# jogo.py
# CRUD da entidade Jogo
# armazenamento em dicionario
# validacoes feitas aqui (nao no main)
# ==============================
from utils import gerar_id_jogo

# lista dos modos aceites
MODOS_VALIDOS = ["single player", "multiplayer", "ambos"]

# dicionario principal onde ficam guardados todos os jogos
# chave: ID gerado automaticamente (ex: J001)
# valor: dicionario com os dados do jogo
jogos = {}

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_jogo(nome, modo, idade_minima, tamanho_gb):

    # valida o modo - loop continua ate ser um dos modos validos
    while modo.lower() not in MODOS_VALIDOS:
        print(f"  Modo invalido. Escolha: {', '.join(MODOS_VALIDOS)}")
        modo = input("  Modo: ")

    # valida a idade - tem de ser um numero inteiro
    # loop continua ate o utilizador introduzir um valor correto
    while True:
        try:
            idade_minima = int(idade_minima)
            break
        except ValueError:
            print("  Idade invalida. Introduz um numero inteiro.")
            idade_minima = input("  Idade minima: ")

    # valida o tamanho - tem de ser um numero (pode ter decimais)
    while True:
        try:
            tamanho_gb = float(tamanho_gb)
            break
        except ValueError:
            print("  Tamanho invalido. Introduz um numero.")
            tamanho_gb = input("  Tamanho (GB): ")

    # gera o ID e guarda o jogo no dicionario
    jid = gerar_id_jogo()
    jogos[jid] = {
        "nome": nome,
        "modo": modo.lower(),           # guarda sempre em minusculas
        "idade_minima": idade_minima,
        "tamanho_gb": tamanho_gb
    }
    print(f"  Jogo criado com sucesso. ID: {jid}")

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_jogos():
    if not jogos:
        print("  Nao existem jogos registados.")
        return
    # percorre todos os pares chave-valor do dicionario
    for jid, dados in jogos.items():
        print(f"  ID: {jid} | Nome: {dados['nome']} | Modo: {dados['modo']} | Idade min.: {dados['idade_minima']}+ | Tamanho: {dados['tamanho_gb']} GB")

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_jogo(jid):
    # loop continua ate o utilizador introduzir um ID existente
    while jid not in jogos:
        print("  Jogo nao encontrado. Tenta novamente.")
        jid = input("  ID do jogo: ")

    dados = jogos[jid]
    print(f"  ID: {jid}")
    print(f"    Nome:        {dados['nome']}")
    print(f"    Modo:        {dados['modo']}")
    print(f"    Idade min.:  {dados['idade_minima']}+")
    print(f"    Tamanho:     {dados['tamanho_gb']} GB")

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_jogo(jid, nome=None, modo=None, idade_minima=None, tamanho_gb=None):
    # loop continua ate o utilizador introduzir um ID existente
    while jid not in jogos:
        print("  Jogo nao encontrado. Tenta novamente.")
        jid = input("  ID do jogo: ")

    # se o modo foi preenchido valida se e um dos modos aceites
    if modo:
        while modo.lower() not in MODOS_VALIDOS:
            print(f"  Modo invalido. Escolha: {', '.join(MODOS_VALIDOS)}")
            modo = input("  Novo modo (enter para manter): ")
            if not modo:
                modo = None
                break

    # se a idade foi preenchida valida se e um numero inteiro
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

    # se o tamanho foi preenchido valida se e um numero
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

    # so atualiza os campos que foram preenchidos (nao None)
    if nome:         jogos[jid]["nome"]         = nome
    if modo:         jogos[jid]["modo"]         = modo.lower()
    if idade_minima: jogos[jid]["idade_minima"] = idade_minima
    if tamanho_gb:   jogos[jid]["tamanho_gb"]   = tamanho_gb
    print("  Jogo atualizado com sucesso.")

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_jogo(jid):
    # loop continua ate o utilizador introduzir um ID existente
    while jid not in jogos:
        print("  Jogo nao encontrado. Tenta novamente.")
        jid = input("  ID do jogo: ")

    del jogos[jid]
    print("  Jogo removido com sucesso.")