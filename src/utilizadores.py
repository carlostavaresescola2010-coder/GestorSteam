# ==============================
#          UTILIZADOR
# CRUD da entidade Utilizador
# armazenamento em dicionario
# validacoes feitas aqui (nao no main)
# retorna codigo no estilo HTTP
# ==============================
from utils import gerar_id_utilizador, validar_data, validar_email

# dicionario principal onde ficam guardados todos os utilizadores
# chave: ID gerado automaticamente (ex: U001)
# valor: dicionario com os dados do utilizador
utilizadores = {}

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_utilizador(nome, username, email, password, nascimento):

    # valida o email - obrigatorio e tem de ter formato correto
    while not validar_email(email):
        print("  Email invalido ou em falta. O email e obrigatorio.")
        email = input("  Email: ")

    # valida a data - formato DD/MM/AAAA e ano entre 1900 e o ano atual
    while not validar_data(nascimento):
        print("  Data invalida. Use DD/MM/AAAA e um ano entre 1900 e o ano atual.")
        nascimento = input("  Data de nascimento (DD/MM/AAAA): ")

    try:
        uid = gerar_id_utilizador()
        utilizadores[uid] = {
            "nome": nome,           # nome verdadeiro da pessoa
            "username": username,   # nome de utilizador na plataforma
            "email": email,
            "password": password,
            "nascimento": nascimento
        }
        # retorna 201 (criado com sucesso) e o ID gerado
        return 201, uid
    except Exception as e:
        # retorna 500 em caso de erro inesperado
        return 500, str(e)

# ── READ - listar todos ────────────────────────────────────────────────────────
def listar_utilizadores():
    if not utilizadores:
        # retorna 404 quando nao existem registos
        return 404, "Nao existem utilizadores registados."

    try:
        for uid, dados in utilizadores.items():
            print(f"  ID: {uid} | Nome: {dados['nome']} | Username: {dados['username']} | Email: {dados['email']} | Nascimento: {dados['nascimento']}")
        # retorna 200 (leitura com sucesso)
        return 200, "Utilizadores listados com sucesso."
    except Exception as e:
        return 500, str(e)

# ── READ - consultar individual ────────────────────────────────────────────────
def consultar_utilizador(uid):
    # loop continua ate o utilizador introduzir um ID existente
    while uid not in utilizadores:
        print("  Utilizador nao encontrado. Tenta novamente.")
        uid = input("  ID do utilizador: ")

    try:
        dados = utilizadores[uid]
        print(f"  ID: {uid}")
        print(f"    Nome:       {dados['nome']}")
        print(f"    Username:   {dados['username']}")
        print(f"    Email:      {dados['email']}")
        # mostra a password mascarada com asteriscos por seguranca
        print(f"    Password:   {'*' * len(dados['password'])}")
        print(f"    Nascimento: {dados['nascimento']}")
        # retorna 200 (leitura com sucesso)
        return 200, "Utilizador consultado com sucesso."
    except Exception as e:
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_utilizador(uid, nome=None, username=None, email=None, password=None, nascimento=None):
    # loop continua ate o utilizador introduzir um ID existente
    while uid not in utilizadores:
        print("  Utilizador nao encontrado. Tenta novamente.")
        uid = input("  ID do utilizador: ")

    try:
        # valida o email se foi preenchido
        if email:
            while not validar_email(email):
                print("  Email invalido.")
                email = input("  Novo email (enter para manter): ")
                if not email:
                    email = None
                    break

        # valida a data se foi preenchida
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

        # retorna 200 (atualizado com sucesso)
        return 200, "Utilizador atualizado com sucesso."
    except Exception as e:
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_utilizador(uid):
    # loop continua ate o utilizador introduzir um ID existente
    while uid not in utilizadores:
        print("  Utilizador nao encontrado. Tenta novamente.")
        uid = input("  ID do utilizador: ")

    try:
        del utilizadores[uid]
        # retorna 200 (removido com sucesso)
        return 200, "Utilizador removido com sucesso."
    except Exception as e:
        return 500, str(e)
