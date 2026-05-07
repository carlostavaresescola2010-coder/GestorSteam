# ==============================
# utils.py
# funcoes auxiliares partilhadas
# por todos os outros ficheiros
# ==============================
from datetime import datetime

# contadores globais para gerar IDs unicos automaticamente
contador_utilizadores = 1
contador_jogos        = 1
contador_loja         = 1
contador_compras      = 1

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

# gera um ID para item da loja no formato L001, L002, ...
def gerar_id_loja():
    global contador_loja
    novo_id = f"L{contador_loja:03d}"
    contador_loja += 1
    return novo_id

# gera um ID para compra no formato C001, C002, ...
def gerar_id_compra():
    global contador_compras
    novo_id = f"C{contador_compras:03d}"
    contador_compras += 1
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