# ==============================
#          UTILS
# ==============================
from datetime import datetime

# contadores globais para gerar IDs unicos automaticamente
contador_utilizadores = 1
contador_jogos = 1

# gera um ID para utilizador no formato U001, U002, ...
def gerar_id_utilizador():
    global contador_utilizadores
    novo_id = f"U{contador_utilizadores:03d}"
    contador_utilizadores += 1
    return novo_id

# gera um ID para jogo no formato J001, J002, ...
def gerar_id_jogo():
    global contador_jogos
    novo_id = f"J{contador_jogos:03d}"
    contador_jogos += 1
    return novo_id

# valida se a data esta no formato DD/MM/AAAA
# e se o ano esta entre 1900 e o ano atual
def validar_data(data_texto):
    try:
        data = datetime.strptime(data_texto, "%d/%m/%Y")
        ano_atual = datetime.now().year
        if data.year < 1900 or data.year > ano_atual:
            return False
        return True
    except ValueError:
        return False

# valida se o email tem formato basico correto (contem @ e . apos o @)
def validar_email(email):
    return "@" in email and "." in email.split("@")[-1]
