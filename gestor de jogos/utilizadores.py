# ==============================
# utilizador.py
# CRUD da entidade Utilizador
# armazenamento em dicionario
# validacoes feitas aqui (nao no main)
# ==============================
from utils import gerar_id_utilizador, validar_data

utilizadores = {}

# CREATE
def criar_utilizador(nome, email, password, nascimento):
    while not validar_data(nascimento):
        print("  Data invalida. Use o formato DD/MM/AAAA.")
        nascimento = input("  Data de nascimento (DD/MM/AAAA): ")
    uid = gerar_id_utilizador()
    utilizadores[uid] = {
        "nome": nome,
        "email": email,
        "password": password,
        "nascimento": nascimento
    }
    print(f"  Utilizador criado com sucesso. ID: {uid}")

# READ - listar todos
def listar_utilizadores():
    if not utilizadores:
        print("  Nao existem utilizadores registados.")
        return
    for uid, dados in utilizadores.items():
        print(f"  ID: {uid} | Nome: {dados['nome']} | Email: {dados['email']} | Nascimento: {dados['nascimento']}")

# READ - consultar individual
def consultar_utilizador(uid):
    if uid not in utilizadores:
        print("  Utilizador nao encontrado.")
        return
    dados = utilizadores[uid]
    print(f"  ID: {uid}")
    print(f"    Nome:       {dados['nome']}")
    print(f"    Email:      {dados['email']}")
    print(f"    Password:   {'*' * len(dados['password'])}")
    print(f"    Nascimento: {dados['nascimento']}")

# UPDATE
def atualizar_utilizador(uid, nome=None, email=None, password=None, nascimento=None):
    if uid not in utilizadores:
        print("  Utilizador nao encontrado.")
        return
    if nascimento:
        while not validar_data(nascimento):
            print("  Data invalida. Use o formato DD/MM/AAAA.")
            nascimento = input("  Nova data DD/MM/AAAA (enter para manter): ")
            if not nascimento:
                nascimento = None
                break
    if nome:       utilizadores[uid]["nome"]       = nome
    if email:      utilizadores[uid]["email"]      = email
    if password:   utilizadores[uid]["password"]   = password
    if nascimento: utilizadores[uid]["nascimento"] = nascimento
    print("  Utilizador atualizado com sucesso.")

# DELETE
def remover_utilizador(uid):
    if uid not in utilizadores:
        print("  Utilizador nao encontrado.")
        return
    del utilizadores[uid]
    print("  Utilizador removido com sucesso.")