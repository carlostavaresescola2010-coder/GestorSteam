# ==============================
# utilizador.py
# CRUD da entidade Utilizador
# armazenamento em dicionario
# validacoes feitas aqui (nao no main)
# ==============================
from utils import gerar_id_utilizador, validar_data, validar_email

# dicionario principal onde ficam guardados todos os utilizadores
# chave: ID gerado automaticamente (ex: U001)
# valor: dicionario com os dados do utilizador
utilizadores = {}

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_utilizador(nome, username, email, password, nascimento):

    # valida o email - obrigatorio e tem de ter formato correto
    # loop continua ate o utilizador introduzir um email valido
    while not validar_email(email):
        print("  Email invalido ou em falta. O email e obrigatorio.")
        email = input("  Email: ")

    # valida a data - tem de estar no formato DD/MM/AAAA
    # e o ano tem de ser entre 1900 e o ano atual
    while not validar_data(nascimento):
        print("  Data invalida. Use DD/MM/AAAA e um ano entre 1900 e o ano atual.")
        nascimento = input("  Data de nascimento (DD/MM/AAAA): ")

    # gera o ID e guarda o utilizador no dicionario
    uid = gerar_id_utilizador()
    utilizadores[uid] = {
        "nome": nome,           # nome verdadeiro da pessoa
        "username": username,   # nome de utilizador na plataforma
        "email": email,
        "password": password,
        "nascimento": nascimento
    }
    print(f"  Utilizador criado com sucesso. ID: {uid}")

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_utilizadores():
    if not utilizadores:
        print("  Nao existem utilizadores registados.")
        return
    # percorre todos os pares chave-valor do dicionario
    for uid, dados in utilizadores.items():
        print(f"  ID: {uid} | Nome: {dados['nome']} | Username: {dados['username']} | Email: {dados['email']} | Nascimento: {dados['nascimento']}")

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_utilizador(uid):
    # loop continua ate o utilizador introduzir um ID existente
    while uid not in utilizadores:
        print("  Utilizador nao encontrado. Tenta novamente.")
        uid = input("  ID do utilizador: ")

    # mostra os detalhes do utilizador encontrado
    dados = utilizadores[uid]
    print(f"  ID: {uid}")
    print(f"    Nome:       {dados['nome']}")
    print(f"    Username:   {dados['username']}")
    print(f"    Email:      {dados['email']}")
    # mostra a password mascarada com asteriscos por seguranca
    print(f"    Password:   {'*' * len(dados['password'])}")
    print(f"    Nascimento: {dados['nascimento']}")

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_utilizador(uid, nome=None, username=None, email=None, password=None, nascimento=None):
    # loop continua ate o utilizador introduzir um ID existente
    while uid not in utilizadores:
        print("  Utilizador nao encontrado. Tenta novamente.")
        uid = input("  ID do utilizador: ")

    # se o email foi preenchido valida o formato
    # loop continua ate ser valido
    if email:
        while not validar_email(email):
            print("  Email invalido. O email e obrigatorio e tem de ter formato correto.")
            email = input("  Novo email (enter para manter): ")
            if not email:
                email = None
                break

    # se a data foi preenchida valida o formato e o ano
    # loop continua ate ser valida ou o utilizador deixar em branco
    if nascimento:
        while not validar_data(nascimento):
            print("  Data invalida. Use DD/MM/AAAA e um ano entre 1900 e o ano atual.")
            nascimento = input("  Nova data DD/MM/AAAA (enter para manter): ")
            if not nascimento:
                nascimento = None
                break

    # so atualiza os campos que foram preenchidos (nao None)
    if nome:       utilizadores[uid]["nome"]       = nome
    if username:   utilizadores[uid]["username"]   = username
    if email:      utilizadores[uid]["email"]      = email
    if password:   utilizadores[uid]["password"]   = password
    if nascimento: utilizadores[uid]["nascimento"] = nascimento
    print("  Utilizador atualizado com sucesso.")

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_utilizador(uid):
    # loop continua ate o utilizador introduzir um ID existente
    while uid not in utilizadores:
        print("  Utilizador nao encontrado. Tenta novamente.")
        uid = input("  ID do utilizador: ")

    del utilizadores[uid]
    print("  Utilizador removido com sucesso.")