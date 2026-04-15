# ==============================
#           JOGO
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

    # valida o modo
    if modo.lower() not in MODOS_VALIDOS:
        return 400, f"Modo invalido. Escolha: {', '.join(MODOS_VALIDOS)}"

    # valida a idade - tem de ser um numero inteiro
    try:
        idade_minima = int(idade_minima)
    except ValueError:
        return 400, "Idade invalida. Introduz um numero inteiro."

    # valida o tamanho - tem de ser um numero
    try:
        tamanho_gb = float(tamanho_gb)
    except ValueError:
        return 400, "Tamanho invalido. Introduz um numero."

    try:
        jid = gerar_id_jogo()
        jogos[jid] = {
            "nome": nome,
            "modo": modo.lower(),           # guarda sempre em minusculas
            "idade_minima": idade_minima,
            "tamanho_gb": tamanho_gb
        }
        return (201, jid)
    except Exception as e:
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_jogos():
    if not jogos:
        return 404, "Nao existem jogos registados."

    try:
        for jid, dados in jogos.items():
            print(f"  ID: {jid} | Nome: {dados['nome']} | Modo: {dados['modo']} | Idade min.: {dados['idade_minima']}+ | Tamanho: {dados['tamanho_gb']} GB")
        return 200, "Jogos listados com sucesso."
    except Exception as e:
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_jogo(jid):
    # retorna 404 se o ID nao existir
    if jid not in jogos:
        return 404, "Jogo nao encontrado."

    try:
        dados = jogos[jid]
        print(f"  ID: {jid}")
        print(f"    Nome:        {dados['nome']}")
        print(f"    Modo:        {dados['modo']}")
        print(f"    Idade min.:  {dados['idade_minima']}+")
        print(f"    Tamanho:     {dados['tamanho_gb']} GB")
        return (200, "Jogo consultado com sucesso.")
    except Exception as e:
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_jogo(jid, nome=None, modo=None, idade_minima=None, tamanho_gb=None):
    # retorna 404 se o ID nao existir
    if jid not in jogos:
        return 404, "Jogo nao encontrado."

    try:
        # valida o modo se foi preenchido
        if modo and modo.lower() not in MODOS_VALIDOS:
            return 400, f"Modo invalido. Escolha: {', '.join(MODOS_VALIDOS)}"

        # valida a idade se foi preenchida
        if idade_minima:
            try:
                idade_minima = int(idade_minima)
            except ValueError:
                return 400, "Idade invalida. Introduz um numero inteiro."

        # valida o tamanho se foi preenchido
        if tamanho_gb:
            try:
                tamanho_gb = float(tamanho_gb)
            except ValueError:
                return 400, "Tamanho invalido. Introduz um numero."

        # so atualiza os campos que foram preenchidos (nao None)
        if nome:         jogos[jid]["nome"]         = nome
        if modo:         jogos[jid]["modo"]         = modo.lower()
        if idade_minima: jogos[jid]["idade_minima"] = idade_minima
        if tamanho_gb:   jogos[jid]["tamanho_gb"]   = tamanho_gb

        return 200, "Jogo atualizado com sucesso."
    except Exception as e:
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_jogo(jid):
    # retorna 404 se o ID nao existir
    if jid not in jogos:
        return 404, "Jogo nao encontrado."

    try:
        del jogos[jid]
        return 200, "Jogo removido com sucesso."
    except Exception as e:
        return 500, str(e)
