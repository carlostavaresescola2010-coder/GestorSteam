# ==============================
# utilizadores.py
# CRUD da entidade Utilizador
# armazenamento em dicionario + persistencia JSON
# validacoes feitas aqui (nao no main)
# retorna codigos de estado ao estilo HTTP
# ==============================
import json
import os
from utils import gerar_id_utilizador, validar_data, validar_email

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
    else:
        utilizadores = {}
    return utilizadores

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_utilizador(nome, username, email, password, nascimento):
    carregar_utilizadores()

    if not validar_email(email):
        return 400, "Email invalido. O email e obrigatorio e tem de ter formato correto."

    if not validar_data(nascimento):
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
        return 201, utilizador
    except Exception as e:
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_utilizadores():
    carregar_utilizadores()
    if not utilizadores:
        return 404, "Nao existem utilizadores registados."

    try:
        return 200, utilizadores
    except Exception as e:
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_utilizador(uid):
    carregar_utilizadores()
    if uid not in utilizadores:
        return 404, "Utilizador nao encontrado."

    try:
        return 200, utilizadores[uid]
    except Exception as e:
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_utilizador(uid, nome=None, username=None, email=None, password=None, nascimento=None):
    carregar_utilizadores()
    if uid not in utilizadores:
        return 404, "Utilizador nao encontrado."

    try:
        if email and not validar_email(email):
            return 400, "Email invalido."

        if nascimento and not validar_data(nascimento):
            return 400, "Data invalida. Use DD-MM-AAAA e um ano entre 1900 e o ano atual."

        if nome:       utilizadores[uid]["nome"]       = nome
        if username:   utilizadores[uid]["username"]   = username
        if email:      utilizadores[uid]["email"]      = email
        if password:   utilizadores[uid]["password"]   = password
        if nascimento: utilizadores[uid]["nascimento"] = nascimento

        guardar_utilizadores()
        return 200, utilizadores[uid]
    except Exception as e:
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_utilizador(uid):
    carregar_utilizadores()
    if uid not in utilizadores:
        return 404, "Utilizador nao encontrado."

    try:
        del utilizadores[uid]
        guardar_utilizadores()
        return 200, uid
    except Exception as e:
        return 500, str(e)