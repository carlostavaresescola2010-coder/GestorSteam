# ==============================
# compras.py
# CRUD da entidade Compra
# representa uma transacao de um utilizador
# que compra um jogo disponivel na loja
# armazenamento em dicionario
# validacoes feitas aqui (nao no main)
# retorna codigos de estado ao estilo HTTP
# ==============================
from utils import gerar_id_compra, validar_data
from utilizadores import utilizadores
from loja import lojas

# dicionario principal onde ficam guardadas todas as compras
# chave: ID gerado automaticamente (ex: C001)
# valor: dicionario com os dados da compra
compras = {}

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_compra(uid, lid, data_compra):

    # valida se o utilizador existe
    if uid not in utilizadores:
        return 404, "Utilizador nao encontrado."

    # valida se o item existe na loja
    if lid not in lojas:
        return 404, "Item nao encontrado na loja."

    # valida a data - formato DD/MM/AAAA
    if not validar_data(data_compra):
        return 400, "Data invalida. Use DD/MM/AAAA e um ano entre 1900 e o ano atual."

    # valida se ha stock disponivel
    if lojas[lid]["stock"] <= 0:
        return 400, "Sem stock disponivel para este jogo."

    # valida se o utilizador ja comprou este item
    for cid, dados in compras.items():
        if dados["uid"] == uid and dados["lid"] == lid:
            return 400, f"Este utilizador ja comprou este jogo (Compra ID: {cid})."

    try:
        cid = gerar_id_compra()
        preco_pago = lojas[lid]["preco"]     # guarda o preco no momento da compra

        compras[cid] = {
            "uid": uid,
            "lid": lid,
            "data_compra": data_compra,
            "preco_pago": preco_pago        # preco fixado no momento da compra
        }

        # desconta uma unidade do stock da loja
        lojas[lid]["stock"] -= 1

        return 201, compras[cid]
    except Exception as e:
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_compras():
    if not compras:
        return 404, "Nao existem compras registadas."

    try:

        return 200, compras
    except Exception as e:
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_compra(cid):
    # retorna 404 se o ID nao existir
    if cid not in compras:
        return 404, "Compra nao encontrada."

    try:
        dados = compras[cid]
        return 200, dados
    except Exception as e:
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_compra(cid, data_compra=None):
    # retorna 404 se o ID nao existir
    if cid not in compras:
        return 404, "Compra nao encontrada."

    try:
        # valida a data se foi preenchida
        if data_compra and not validar_data(data_compra):
            return 400, "Data invalida. Use DD/MM/AAAA e um ano entre 1900 e o ano atual."

        # so atualiza os campos que foram preenchidos (nao None)
        # nota: uid, lid e preco_pago nao sao editaveis para manter integridade
        if data_compra: compras[cid]["data_compra"] = data_compra

        return 200, data_compra
    except Exception as e:
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_compra(cid):
    # retorna 404 se o ID nao existir
    if cid not in compras:
        return 404, "Compra nao encontrada."

    try:
        # devolve uma unidade ao stock da loja ao cancelar a compra
        lid = compras[cid]["lid"]
        if lid in lojas:
            lojas[lid]["stock"] += 1

        del compras[cid]
        return 200, cid
    except Exception as e:
        return 500, str(e)