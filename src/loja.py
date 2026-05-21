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
import logging
from utils import gerar_id_loja
from jogos import carregar_jogos

logger = logging.getLogger(__name__)

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
            logger.info(f"Loja carregada: {len(lojas)} itens")
    else:
        lojas = {}
        logger.info("Ficheiro da loja nao encontrado, iniciando vazio")
    return lojas

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_item_loja(jid, preco, stock):
    carregar_loja()
    jogos = carregar_jogos()

    if jid not in jogos:
        logger.warning(f"Tentativa de adicionar item da loja com jogo inexistente: {jid}")
        return 404, "Jogo nao encontrado."

    for lid, dados in lojas.items():
        if dados["jid"] == jid:
            logger.warning(f"Jogo {jid} ja esta na loja com ID {lid}")
            return 400, f"Este jogo ja esta na loja com o ID {lid}."

    try:
        preco = float(preco)
        if preco < 0:
            logger.warning(f"Preco negativo fornecido: {preco}")
            return 400, "Preco invalido. O preco nao pode ser negativo."
    except ValueError:
        logger.warning(f"Preco invalido (nao numerico): {preco}")
        return 400, "Preco invalido. Introduz um numero."

    try:
        stock = int(stock)
        if stock < 0:
            logger.warning(f"Stock negativo fornecido: {stock}")
            return 400, "Stock invalido. O stock nao pode ser negativo."
    except ValueError:
        logger.warning(f"Stock invalido (nao inteiro): {stock}")
        return 400, "Stock invalido. Introduz um numero inteiro."

    try:
        lid = gerar_id_loja()
        lojas[lid] = {
            "jid": jid,
            "preco": preco,
            "stock": stock
        }
        guardar_loja()
        logger.info(f"Item da loja criado: {lid} (jogo {jid}, preco {preco}, stock {stock})")
        return 201, lid
    except Exception as e:
        logger.error(f"Erro ao criar item da loja: {str(e)}")
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_loja():
    carregar_loja()
    jogos = carregar_jogos()
    if not lojas:
        logger.info("Listagem da loja: nenhum item na loja")
        return 404, "Nao existem itens na loja."

    try:
        # (mantido o print original)
        for lid, dados in lojas.items():
            nome_jogo = jogos[dados["jid"]]["nome"] if dados["jid"] in jogos else "Jogo removido"
            print(f"  ID: {lid} | Jogo: {nome_jogo} | Preco: {dados['preco']:.2f}€ | Stock: {dados['stock']}")
        logger.info(f"Listagem da loja: {len(lojas)} itens exibidos")
        return 200, lojas
    except Exception as e:
        logger.error(f"Erro ao listar loja: {str(e)}")
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_item_loja(lid):
    carregar_loja()
    if lid not in lojas:
        logger.warning(f"Item da loja nao encontrado: {lid}")
        return 404, "Item nao encontrado na loja."

    try:
        logger.info(f"Consulta do item da loja {lid}")
        return 200, lojas[lid]
    except Exception as e:
        logger.error(f"Erro ao consultar item da loja {lid}: {str(e)}")
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_item_loja(lid, preco=None, stock=None):
    carregar_loja()
    if lid not in lojas:
        logger.warning(f"Tentativa de atualizar item da loja inexistente: {lid}")
        return 404, "Item nao encontrado na loja."

    try:
        if preco is not None:
            try:
                preco = float(preco)
                if preco < 0:
                    logger.warning(f"Preco negativo para atualizacao do item {lid}: {preco}")
                    return 400, "Preco invalido. O preco nao pode ser negativo."
            except ValueError:
                logger.warning(f"Preco invalido (nao numerico) para item {lid}: {preco}")
                return 400, "Preco invalido. Introduz um numero."

        if stock is not None:
            try:
                stock = int(stock)
                if stock < 0:
                    logger.warning(f"Stock negativo para atualizacao do item {lid}: {stock}")
                    return 400, "Stock invalido. O stock nao pode ser negativo."
            except ValueError:
                logger.warning(f"Stock invalido (nao inteiro) para item {lid}: {stock}")
                return 400, "Stock invalido. Introduz um numero inteiro."

        if preco is not None: lojas[lid]["preco"] = preco
        if stock is not None: lojas[lid]["stock"] = stock

        guardar_loja()
        logger.info(f"Item da loja {lid} atualizado: preco={lojas[lid]['preco']}, stock={lojas[lid]['stock']}")
        return 200, lojas[lid]
    except Exception as e:
        logger.error(f"Erro ao atualizar item da loja {lid}: {str(e)}")
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_item_loja(lid):
    carregar_loja()
    if lid not in lojas:
        logger.warning(f"Tentativa de remover item da loja inexistente: {lid}")
        return 404, "Item nao encontrado na loja."

    try:
        del lojas[lid]
        guardar_loja()
        logger.info(f"Item da loja {lid} removido permanentemente")
        return 200, lid
    except Exception as e:
        logger.error(f"Erro ao remover item da loja {lid}: {str(e)}")
        return 500, str(e)