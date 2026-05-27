# ==============================
# utilizadores.py
# CRUD da entidade Utilizador
# armazenamento em dicionario + persistencia JSON
# validacoes feitas aqui (nao no main)
# retorna codigos de estado ao estilo HTTP
# ==============================
import json
import os
import logging
from utils import gerar_id_utilizador, validar_data, validar_email

logger = logging.getLogger(__name__)

FICHEIRO_UTILIZADORES = "utilizadores.json"

# dicionario principal onde ficam guardados todos os utilizadores
utilizadores = {}

# ==========================
# Persistência
# ==========================
def guardar_utilizadores():
    with open(FICHEIRO_UTILIZADORES, "w", encoding="utf-8") as ficheiro:
        json.dump(utilizadores, ficheiro, indent=4, ensure_ascii=False)

def carregar_utilizadores():
    global utilizadores
    if os.path.exists(FICHEIRO_UTILIZADORES):
        with open(FICHEIRO_UTILIZADORES, "r", encoding="utf-8") as ficheiro:
            utilizadores = json.load(ficheiro)
            logger.info(f"Utilizadores carregados: {len(utilizadores)} registos")
    else:
        utilizadores = {}
        logger.info("Ficheiro de utilizadores nao encontrado, iniciando vazio")
    return utilizadores

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_utilizador(nome, username, email, password, nascimento):
    carregar_utilizadores()

    if not validar_email(email):
        logger.error(f"Email invalido fornecido: {email}")
        return 400, "Email invalido. O email e obrigatorio e tem de ter formato correto."

    if not validar_data(nascimento):
        logger.error(f"Data de nascimento invalida: {nascimento}")
        return 400, "Data invalida. Use DD-MM-AAAA e um ano entre 1900 e o ano atual."

    try:
        uid = gerar_id_utilizador()
        utilizador = {
            "nome": nome,
            "username": username,
            "email": email,
            "password": password,
            "nascimento": nascimento,
            "uid": uid
        }
        utilizadores[uid] = utilizador
        guardar_utilizadores()
        logger.info(f"Utilizador criado: {uid} - {username} ({email})")
        return 201, utilizador
    except Exception as e:
        logger.exception(f"Erro ao criar utilizador: {str(e)}")
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_utilizadores():
    carregar_utilizadores()
    if not utilizadores:
        logger.error("Listagem de utilizadores: nenhum utilizador registado")
        return 404, "Nao existem utilizadores registados."

    try:
        logger.info(f"Listagem de utilizadores: {len(utilizadores)} utilizadores retornados")
        return 200, utilizadores
    except Exception as e:
        logger.exception(f"Erro ao listar utilizadores: {str(e)}")
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_utilizador(uid):
    carregar_utilizadores()
    if uid not in utilizadores:
        logger.error(f"Utilizador nao encontrado: {uid}")
        return 404, "Utilizador nao encontrado."

    try:
        logger.info(f"Consulta do utilizador {uid}")
        return 200, utilizadores[uid]
    except Exception as e:
        logger.exception(f"Erro ao consultar utilizador {uid}: {str(e)}")
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_utilizador(uid, nome=None, username=None, email=None, password=None, nascimento=None):
    carregar_utilizadores()
    if uid not in utilizadores:
        logger.error(f"Tentativa de atualizar utilizador inexistente: {uid}")
        return 404, "Utilizador nao encontrado."

    try:
        if email and not validar_email(email):
            logger.error(f"Email invalido para atualizacao do utilizador {uid}: {email}")
            return 400, "Email invalido."

        if nascimento and not validar_data(nascimento):
            logger.error(f"Data invalida para atualizacao do utilizador {uid}: {nascimento}")
            return 400, "Data invalida. Use DD-MM-AAAA e um ano entre 1900 e o ano atual."

        if nome:       utilizadores[uid]["nome"]       = nome
        if username:   utilizadores[uid]["username"]   = username
        if email:      utilizadores[uid]["email"]      = email
        if password:   utilizadores[uid]["password"]   = password
        if nascimento: utilizadores[uid]["nascimento"] = nascimento

        guardar_utilizadores()
        logger.info(f"Utilizador {uid} atualizado: {utilizadores[uid]}")
        return 200, utilizadores[uid]
    except Exception as e:
        logger.exception(f"Erro ao atualizar utilizador {uid}: {str(e)}")
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_utilizador(uid):
    carregar_utilizadores()
    if uid not in utilizadores:
        logger.error(f"Tentativa de remover utilizador inexistente: {uid}")
        return 404, "Utilizador nao encontrado."

    try:
        del utilizadores[uid]
        guardar_utilizadores()
        logger.info(f"Utilizador {uid} removido permanentemente")
        return 200, uid
    except Exception as e:
        logger.exception(f"Erro ao remover utilizador {uid}: {str(e)}")
        return 500, str(e)