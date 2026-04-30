# ==============================
# loja.py
# CRUD da entidade Loja
# representa os jogos disponiveis para compra
# com preco e stock
# armazenamento em dicionario
# validacoes feitas aqui (nao no main)
# retorna codigos de estado ao estilo HTTP
# ==============================
from utils import gerar_id_loja
from jogos import jogos

# dicionario principal onde ficam guardados todos os itens da loja
# chave: ID gerado automaticamente (ex: L001)
# valor: dicionario com os dados do item
lojas = {}

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_item_loja(jid, preco, stock):

    # valida se o jogo existe
    if jid not in jogos:
        return 404, "Jogo nao encontrado."

    # valida se o jogo ja esta na loja
    for lid, dados in lojas.items():
        if dados["jid"] == jid:
            return 400, f"Este jogo ja esta na loja com o ID {lid}."

    # valida o preco - tem de ser um numero positivo
    try:
        preco = float(preco)
        if preco < 0:
            return 400, "Preco invalido. O preco nao pode ser negativo."
    except ValueError:
        return 400, "Preco invalido. Introduz um numero."

    # valida o stock - tem de ser um numero inteiro nao negativo
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
        return 201, lid
    except Exception as e:
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_loja():
    if not lojas:
        return 404, "Nao existem itens na loja."

    try:
        for lid, dados in lojas.items():
            nome_jogo = jogos[dados["jid"]]["nome"] if dados["jid"] in jogos else "Jogo removido"
            print(f"  ID: {lid} | Jogo: {nome_jogo} | Preco: {dados['preco']:.2f}€ | Stock: {dados['stock']}")
        return 200, "Loja listada com sucesso."
    except Exception as e:
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_item_loja(lid):
    # retorna 404 se o ID nao existir
    if lid not in lojas:
        return 404, "Item nao encontrado na loja."

    try:
        return 200, lojas[lid]
    except Exception as e:
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_item_loja(lid, preco=None, stock=None):
    # retorna 404 se o ID nao existir
    if lid not in lojas:
        return 404, "Item nao encontrado na loja."

    try:
        # valida o preco se foi preenchido
        if preco is not None:
            try:
                preco = float(preco)
                if preco < 0:
                    return 400, "Preco invalido. O preco nao pode ser negativo."
            except ValueError:
                return 400, "Preco invalido. Introduz um numero."

        # valida o stock se foi preenchido
        if stock is not None:
            try:
                stock = int(stock)
                if stock < 0:
                    return 400, "Stock invalido. O stock nao pode ser negativo."
            except ValueError:
                return 400, "Stock invalido. Introduz um numero inteiro."

        # so atualiza os campos que foram preenchidos (nao None)
        if preco is not None: lojas[lid]["preco"] = preco
        if stock is not None: lojas[lid]["stock"] = stock

        return 200, "Item da loja atualizado com sucesso."
    except Exception as e:
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_item_loja(lid):
    # retorna 404 se o ID nao existir
    if lid not in lojas:
        return 404, "Item nao encontrado na loja."

    try:
        del lojas[lid]
        return 200, "Item removido da loja com sucesso."
    except Exception as e:
        return 500, str(e)
