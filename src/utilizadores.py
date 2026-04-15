# ==============================
#          UTILIZADOR
# ==============================
from utils import gerar_id_utilizador, validar_data, validar_email

# dicionario principal onde ficam guardados todos os utilizadores
# chave: ID gerado automaticamente (ex: U001)
# valor: dicionario com os dados do utilizador
utilizadores = {}

# ── CREATE ─────────────────────────────────────────────────────────────────────
def criar_utilizador(nome, username, email, password, nascimento):

    # valida o email - obrigatorio e tem de ter formato correto
    if not validar_email(email):
        return 400, "Email invalido. O email e obrigatorio e tem de ter formato correto."

    # valida a data - formato DD/MM/AAAA e ano entre 1900 e o ano atual
    if not validar_data(nascimento):
        return 400, "Data invalida. Use DD/MM/AAAA e um ano entre 1900 e o ano atual."

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
    # retorna 404 se o ID nao existir
    if uid not in utilizadores:
        return 404, "Utilizador nao encontrado."

    try:
        dados = utilizadores[uid]
        print(f"  ID: {uid}")
        print(f"    Nome:       {dados['nome']}")
        print(f"    Username:   {dados['username']}")
        print(f"    Email:      {dados['email']}")
        # mostra a password mascarada com asteriscos por seguranca
        print(f"    Password:   {'*' * len(dados['password'])}")
        print(f"    Nascimento: {dados['nascimento']}")
        return 200, "Utilizador consultado com sucesso."
    except Exception as e:
        return 500, str(e)

# ── UPDATE ─────────────────────────────────────────────────────────────────────
def atualizar_utilizador(uid, nome=None, username=None, email=None, password=None, nascimento=None):
    # retorna 404 se o ID nao existir
    if uid not in utilizadores:
        return 404, "Utilizador nao encontrado."

    try:
        # valida o email se foi preenchido
        if email and not validar_email(email):
            return 400, "Email invalido."

        # valida a data se foi preenchida
        if nascimento and not validar_data(nascimento):
            return 400, "Data invalida. Use DD/MM/AAAA e um ano entre 1900 e o ano atual."

        # so atualiza os campos que foram preenchidos (nao None)
        if nome:       utilizadores[uid]["nome"]       = nome
        if username:   utilizadores[uid]["username"]   = username
        if email:      utilizadores[uid]["email"]      = email
        if password:   utilizadores[uid]["password"]   = password
        if nascimento: utilizadores[uid]["nascimento"] = nascimento

        return 200, "Utilizador atualizado com sucesso."
    except Exception as e:
        return 500, str(e)

# ── DELETE ─────────────────────────────────────────────────────────────────────
def remover_utilizador(uid):
    # retorna 404 se o ID nao existir
    if uid not in utilizadores:
        return 404, "Utilizador nao encontrado."

    try:
        del utilizadores[uid]
        return 200, "Utilizador removido com sucesso."
    except Exception as e:
        return 500, str(e)
