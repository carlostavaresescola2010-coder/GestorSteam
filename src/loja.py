# ==============================
# loja.py
# CRUD da entidade Loja
# representa os jogos disponiveis para compra
# com preco e stock
# armazenamento em dicionario + persistencia JSON
# validacoes feitas aqui (nao no main)
# retorna codigos de estado ao estilo HTTP
# ==============================
import json
import os
from utils import gerar_id_loja
from jogos import jogos, carregar_jogos

FICHEIRO_LOJA = "loja.json"

# dicionario principal onde ficam guardados todos os itens da loja
lojas = {}

# ==========================
# Persistência
# ==========================
def guardar_loja():
    with open(FICHEIRO_LOJA, "w", encoding="utf-8") as ficheiro:
        json.dump(lojas, ficheiro, indent=4, ensure_ascii=False)

def carregar_loja():
    global lojas
    if os.path.exists(FICHEIRO_LOJA):
        with open(FICHEIRO_LOJA, "r", encoding="utf-8") as ficheiro:
            lojas = json.load(ficheiro)
    else:
        lojas = {}

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_item_loja(jid, preco, stock):
    carregar_loja()
    carregar_jogos()

    if jid not in jogos:
        return 404, "Jogo nao encontrado."

    for lid, dados in lojas.items():
        if dados["jid"] == jid:
            return 400, f"Este jogo ja esta na loja com o ID {lid}."

    try:
        preco = float(preco)
        if preco < 0:
            return 400, "Preco invalido. O preco nao pode ser negativo."
    except ValueError:
        return 400, "Preco invalido. Introduz um numero."

    try:
        stock = int(stock)
        if stock < 0:
            return 400, "Stock invalido. O stock nao pode ser negativo."
    except ValueError:
        return 400, "Stock invalido. Introduz um numero inteiro."

    try:
        lid = gerar_id_loja()
        lojas[lid] = {
            "jid": jid,
            "preco": preco,
            "stock": stock
        }
        guardar_loja()
        return 201, lid
    except Exception as e:
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_loja():
    carregar_loja()
    carregar_jogos()
    if not lojas:
        return 404, "Nao existem itens na loja."

    try:
        for lid, dados in lojas.items():
            nome_jogo = jogos[dados["jid"]]["nome"] if dados["jid"] in jogos else "Jogo removido"
            print(f"  ID: {lid} | Jogo: {nome_jogo} | Preco: {dados['preco']:.2f}€ | Stock: {dados['stock']}")
        return 200, lojas
    except Exception as e:
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_item_loja(lid):
    carregar_loja()
    if lid not in lojas:
        return 404, "Item nao encontrado na loja."

    try:
        return 200, lojas[lid]
    except Exception as e:
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_item_loja(lid, preco=None, stock=None):
    carregar_loja()
    if lid not in lojas:
        return 404, "Item nao encontrado na loja."

    try:
        if preco is not None:
            try:
                preco = float(preco)
                if preco < 0:
                    return 400, "Preco invalido. O preco nao pode ser negativo."
            except ValueError:
                return 400, "Preco invalido. Introduz um numero."

        if stock is not None:
            try:
                stock = int(stock)
                if stock < 0:
                    return 400, "Stock invalido. O stock nao pode ser negativo."
            except ValueError:
                return 400, "Stock invalido. Introduz um numero inteiro."

        if preco is not None: lojas[lid]["preco"] = preco
        if stock is not None: lojas[lid]["stock"] = stock

        guardar_loja()
        return 200, lojas[lid]
    except Exception as e:
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_item_loja(lid):
    carregar_loja()
    if lid not in lojas:
        return 404, "Item nao encontrado na loja."

    try:
        del lojas[lid]
        guardar_loja()
        return 200, lid
    except Exception as e:
        return 500, str(e)
