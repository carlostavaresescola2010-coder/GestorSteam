# ==============================
# jogos.py
# CRUD da entidade Jogo
# armazenamento em dicionario + persistencia JSON
# validacoes feitas aqui (nao no main)
# retorna codigos de estado ao estilo HTTP
# ==============================
import json
import os
import logging
from utils import gerar_id_jogo

logger = logging.getLogger(__name__)

FICHEIRO_JOGOS = "jogos.json"

MODOS_VALIDOS = ["single player", "multiplayer", "ambos"]

# dicionario principal onde ficam guardados todos os jogos
jogos = {}

# ==========================
# Persistência
# ==========================
def guardar_jogos():
    with open(FICHEIRO_JOGOS, "w", encoding="utf-8") as ficheiro:
        json.dump(jogos, ficheiro, indent=4, ensure_ascii=False)

def carregar_jogos():
    global jogos
    if os.path.exists(FICHEIRO_JOGOS):
        with open(FICHEIRO_JOGOS, "r", encoding="utf-8") as ficheiro:
            jogos = json.load(ficheiro)
            logger.info(f"Jogos carregados: {len(jogos)} registos")
    else:
        jogos = {}
        logger.info("Ficheiro de jogos nao encontrado, iniciando vazio")
    return jogos

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_jogo(nome, modo, idade_minima, tamanho_gb):
    carregar_jogos()

    if modo.lower() not in MODOS_VALIDOS:
        logger.error(f"Tentativa de criar jogo com modo invalido: {modo}")
        return 400, f"Modo invalido. Escolha: {', '.join(MODOS_VALIDOS)}"

    try:
        idade_minima = int(idade_minima)
    except ValueError:
        logger.warning(f"Idade invalida fornecida: {idade_minima}")
        return 400, "Idade invalida. Introduz um numero inteiro."

    try:
        tamanho_gb = float(tamanho_gb)
    except ValueError:
        logger.error(f"Tamanho invalido fornecida: {tamanho_gb}")
        return 400, "Tamanho invalido. Introduz um numero."

    try:
        jid = gerar_id_jogo()
        jogos[jid] = {
            "nome": nome,
            "modo": modo.lower(),
            "idade_minima": idade_minima,
            "tamanho_gb": tamanho_gb
        }
        guardar_jogos()
        logger.info(f"Jogo criado: {jid} - {nome} (modo {modo}, idade minima {idade_minima}, tamanho {tamanho_gb}GB)")
        return 201, jogos[jid]
    except Exception as e:
        logger.exception(f"Erro ao criar jogo: {str(e)}")
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_jogos():
    carregar_jogos()
    if not jogos:
        logger.info("Listagem de jogos: nenhum jogo registado")
        return 404, "Nao existem jogos registados."

    try:
        logger.info(f"Listagem de jogos: {len(jogos)} jogos retornados")
        return 200, jogos
    except Exception as e:
        logger.exception(f"Erro ao listar jogos: {str(e)}")
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_jogo(jid):
    carregar_jogos()
    if jid not in jogos:
        logger.error(f"Jogo nao encontrado: {jid}")
        return 404, "Jogo nao encontrado."

    try:
        logger.info(f"Consulta do jogo {jid}")
        return 200, jogos[jid]
    except Exception as e:
        logger.exception(f"Erro ao consultar jogo {jid}: {str(e)}")
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_jogo(jid, nome=None, modo=None, idade_minima=None, tamanho_gb=None):
    carregar_jogos()
    if jid not in jogos:
        logger.error(f"Tentativa de atualizar jogo inexistente: {jid}")
        return 404, "Jogo nao encontrado."

    try:
        if modo and modo.lower() not in MODOS_VALIDOS:
            logger.error(f"Modo invalido para atualizacao do jogo {jid}: {modo}")
            return 400, f"Modo invalido. Escolha: {', '.join(MODOS_VALIDOS)}"

        if idade_minima:
            try:
                idade_minima = int(idade_minima)
            except ValueError:
                logger.error(f"Idade invalida para atualizacao do jogo {jid}: {idade_minima}")
                return 400, "Idade invalida. Introduz um numero inteiro."

        if tamanho_gb:
            try:
                tamanho_gb = float(tamanho_gb)
            except ValueError:
                logger.error(f"Tamanho invalido para atualizacao do jogo {jid}: {tamanho_gb}")
                return 400, "Tamanho invalido. Introduz um numero."

        if nome:         jogos[jid]["nome"]         = nome
        if modo:         jogos[jid]["modo"]         = modo.lower()
        if idade_minima: jogos[jid]["idade_minima"] = idade_minima
        if tamanho_gb:   jogos[jid]["tamanho_gb"]   = tamanho_gb

        guardar_jogos()
        logger.info(f"Jogo {jid} atualizado: {jogos[jid]}")
        return 200, jogos[jid]
    except Exception as e:
        logger.exception(f"Erro ao atualizar jogo {jid}: {str(e)}")
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_jogo(jid):
    carregar_jogos()
    if jid not in jogos:
        logger.error(f"Tentativa de remover jogo inexistente: {jid}")
        return 404, "Jogo nao encontrado."

    try:
        del jogos[jid]
        guardar_jogos()
        logger.info(f"Jogo {jid} removido permanentemente")
        return 200, jid
    except Exception as e:
        logger.exception(f"Erro ao remover jogo {jid}: {str(e)}")
        return 500, str(e)