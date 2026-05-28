import tkinter as tk
from tkinter import messagebox

# =====================
# DADOS
# =====================



produtos = []  # (id, nome, preco, quantidade)
dinheiro = 3000
proximo_id = 1  #ID automático
mes = 1

compras_mes = 0 #total compras
vendas_mes = 0  #total vendas


# =====================
# FUNÇÕES
# =====================

def atualizar_status(): #atualiza o cabeçario
    status.config(text=f"Mês: {mes} | Dinheiro: {dinheiro:.2f}€")


def listar_todos():
    lista.delete(0, tk.END) #limpa a lista
    for p in produtos: #percorre; interface
        lista.insert(tk.END, f"ID {p[0]} | {p[1]} | {p[3]} unidades")


def listar_por_quantidade(): #limpa; ordenados
    lista.delete(0, tk.END)
    ordenado = sorted(produtos, key=lambda x: x[3], reverse=True) #ordena; maior para menor
    for p in ordenado:
        lista.insert(tk.END, f"{p[1]} - {p[3]} unidades")


def adicionar():
    global dinheiro, proximo_id, compras_mes #global para mudar as variaveis

    nome = entry_nome.get()
    preco = entry_preco.get()
    qtd = entry_qtd.get()

    if nome == "" or preco == "" or qtd == "":
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    if not preco.replace(".", "", 1).isdigit() or not qtd.isdigit(): #decimais
        messagebox.showerror("Erro", "Preço e quantidade devem ser números.")
        return

    preco = float(preco)
    qtd = int(qtd)

    custo = preco * qtd #custo total



    if custo > dinheiro:
        messagebox.showerror("Erro", "Dinheiro insuficiente.")
        return

    dinheiro -= custo
    compras_mes += custo

    produtos.append((proximo_id, nome, preco, qtd)) #guardado como tupla
    proximo_id += 1

    atualizar_status()
    listar_todos()
    messagebox.showinfo("Sucesso", "Produto adicionado!")


def vender():
    global dinheiro, vendas_mes

    id_prod = entry_id.get()
    qtd = entry_qtd_venda.get()

    if not id_prod.isdigit() or not qtd.isdigit(): # verifica se tem números
        messagebox.showerror("Erro", "ID e quantidade devem ser números.")
        return

    id_prod = int(id_prod)
    qtd = int(qtd)

    for i, p in enumerate(produtos):
        if p[0] == id_prod:
            if qtd > p[3]:
                messagebox.showerror("Erro", "Estoque insuficiente.")
                return

            total = p[2] * qtd
            dinheiro += total
            vendas_mes += total

            nova_qtd = p[3] - qtd
            produtos[i] = (p[0], p[1], p[2], nova_qtd) #substituir tudo

            atualizar_status()
            listar_todos()
            messagebox.showinfo("Venda", "Venda realizada!")
            return

    messagebox.showerror("Erro", "Produto não encontrado.")


def mostrar_estatisticas():
    lucro = vendas_mes - compras_mes

    messagebox.showinfo(
        "Estatísticas do Mês",
        f"Total Compras: {compras_mes:.2f}€\n"
        f"Total Vendas: {vendas_mes:.2f}€\n"
        f"Lucro do Mês: {lucro:.2f}€"
    )


def avancar_mes():
    global mes, compras_mes, vendas_mes
    mes += 1
    #reinicia
    compras_mes = 0
    vendas_mes = 0
    atualizar_status()
    messagebox.showinfo("Tempo", "Novo mês iniciado!")


# =====================
# INTERFACE
# =====================

janela = tk.Tk()
janela.title("Empresa Simples") #titulo na janela
janela.geometry("600x500") #tamanho da janela

status = tk.Label(janela, font=("Arial", 12, "bold"))
status.pack(pady=10)

# ---- Adicionar ----
frame1 = tk.LabelFrame(janela, text="Adicionar Produto")
frame1.pack(pady=10, fill="x", padx=10)

tk.Label(frame1, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(frame1)
entry_nome.grid(row=0, column=1)

tk.Label(frame1, text="Preço").grid(row=0, column=2)
entry_preco = tk.Entry(frame1)
entry_preco.grid(row=0, column=3)

tk.Label(frame1, text="Quantidade").grid(row=0, column=4)
entry_qtd = tk.Entry(frame1)
entry_qtd.grid(row=0, column=5)

tk.Button(frame1, text="Adicionar", command=adicionar).grid(row=0, column=6, padx=10)

# ---- Vender ----
frame2 = tk.LabelFrame(janela, text="Vender Produto")
frame2.pack(pady=10, fill="x", padx=10)

tk.Label(frame2, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(frame2)
entry_id.grid(row=0, column=1)

tk.Label(frame2, text="Quantidade").grid(row=0, column=2)
entry_qtd_venda = tk.Entry(frame2)
entry_qtd_venda.grid(row=0, column=3)

tk.Button(frame2, text="Vender", command=vender).grid(row=0, column=4, padx=10)

# ---- Lista ----
lista = tk.Listbox(janela, width=70, height=10)
lista.pack(pady=15)

tk.Button(janela, text="Listar Todos", command=listar_todos).pack(pady=2)
tk.Button(janela, text="Listar por Quantidade", command=listar_por_quantidade).pack(pady=2)
tk.Button(janela, text="Estatísticas do Mês", command=mostrar_estatisticas).pack(pady=2)
tk.Button(janela, text="Avançar Mês", command=avancar_mes).pack(pady=5)

atualizar_status()
janela.mainu loop()