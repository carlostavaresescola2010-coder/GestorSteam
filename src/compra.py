# ==============================
# compra.py
# CRUD da entidade Compra
# representa uma transacao de um utilizador
# que compra um jogo disponivel na loja
# armazenamento em dicionario + persistencia JSON
# validacoes feitas aqui (nao no main)
# retorna codigos de estado ao estilo HTTP
# ==============================
import json
import os
from utils import gerar_id_compra, validar_data
from utilizadores import carregar_utilizadores
from loja import carregar_loja, guardar_loja

FICHEIRO_COMPRAS = "compras.json"

# dicionario principal onde ficam guardadas todas as compras
compras = {}

# ==========================
# Persistência
# ==========================
def guardar_compras():
    with open(FICHEIRO_COMPRAS, "w", encoding="utf-8") as ficheiro:
        json.dump(compras, ficheiro, indent=4, ensure_ascii=False)

def carregar_compras():
    global compras
    if os.path.exists(FICHEIRO_COMPRAS):
        with open(FICHEIRO_COMPRAS, "r", encoding="utf-8") as ficheiro:
            compras = json.load(ficheiro)
    else:
        compras = {}
    return compras

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_compra(uid, lid, data_compra):
    carregar_compras()
    utilizadores = carregar_utilizadores()  # fora do seu ambito - captura o retorno
    lojas = carregar_loja()                 # fora do seu ambito - captura o retorno

    if uid not in utilizadores:
        return 404, "Utilizador nao encontrado."

    if lid not in lojas:
        return 404, "Item nao encontrado na loja."

    if not validar_data(data_compra):
        return 400, "Data invalida. Use DD-MM-AAAA e um ano entre 1900 e o ano atual."

    if lojas[lid]["stock"] <= 0:
        return 400, "Sem stock disponivel para este jogo."

    for cid, dados in compras.items():
        if dados["uid"] == uid and dados["lid"] == lid:
            return 400, f"Este utilizador ja comprou este jogo (Compra ID: {cid})."

    try:
        cid = gerar_id_compra()
        preco_pago = lojas[lid]["preco"]

        compras[cid] = {
            "uid": uid,
            "lid": lid,
            "data_compra": data_compra,
            "preco_pago": preco_pago
        }

        lojas[lid]["stock"] -= 1

        guardar_compras()
        guardar_loja()
        return 201, cid
    except Exception as e:
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_compras():
    carregar_compras()
    if not compras:
        return 404, "Nao existem compras registadas."

    try:
        return 200, compras
    except Exception as e:
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_compra(cid):
    carregar_compras()
    utilizadores = carregar_utilizadores()  # fora do seu ambito - captura o retorno
    if cid not in compras:
        return 404, "Compra nao encontrada."

    try:
        dados = compras[cid]
        uid = dados["uid"]
        username = utilizadores[uid]["username"] if uid in utilizadores else "Utilizador removido"
        return 200, {**dados, "username": username}
    except Exception as e:
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_compra(cid, data_compra=None):
    carregar_compras()
    if cid not in compras:
        return 404, "Compra nao encontrada."

    try:
        if data_compra and not validar_data(data_compra):
            return 400, "Data invalida. Use DD-MM-AAAA e um ano entre 1900 e o ano atual."

        if data_compra: compras[cid]["data_compra"] = data_compra

        guardar_compras()
        return 200, data_compra
    except Exception as e:
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_compra(cid):
    carregar_compras()
    lojas = carregar_loja()  # fora do seu ambito - captura o retorno
    if cid not in compras:
        return 404, "Compra nao encontrada."

    try:
        lid = compras[cid]["lid"]
        if lid in lojas:
            lojas[lid]["stock"] += 1
            guardar_loja()

        del compras[cid]
        guardar_compras()
        return 200, cid
    except Exception as e:
        return 500, str(e)