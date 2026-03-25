# ==============================
# utils.py
# funções auxiliares
# ==============================
from datetime import datetime

contador_utilizadores = 1
contador_jogos = 1

def gerar_id_utilizador():
    global contador_utilizadores
    novo_id = f"U{contador_utilizadores:03d}"
    contador_utilizadores += 1
    return novo_id

def gerar_id_jogo():
    global contador_jogos
    novo_id = f"J{contador_jogos:03d}"
    contador_jogos += 1
    return novo_id

def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, "%d/%m/%Y")
        return True
    except ValueError:
        return False