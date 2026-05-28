import tkinter as tk
from tkinter import messagebox

# ==============================
# DADOS DA EMPRESA
# ==============================

# Produto = (id, nome, preco_compra, preco_venda, quantidade)

produtos = []
dinheiro = 10000.0
proximo_id = 1

mes_atual = 1
ano_atual = 1

compras_mes = 0.0
vendas_mes = 0.0
compras_ano = 0.0
vendas_ano = 0.0


# ==============================
# FUNÇÕES
# ==============================

def atualizar_status():
    status_label.config(
        text=f"Ano: {ano_atual} | Mês: {mes_atual} | Dinheiro: {dinheiro:.2f}€"
    )


def listar_produtos():
    lista.delete(0, tk.END)
    for p in produtos:
        lista.insert(tk.END,
                     f"ID:{p[0]} | {p[1]} | Compra:{p[2]}€ | Venda:{p[3]}€ | Qtd:{p[4]}")


def comprar_produto():
    global dinheiro, proximo_id, compras_mes, compras_ano

    try:
        nome = entry_nome.get().strip()
        preco_compra = float(entry_compra.get())
        preco_venda = float(entry_venda.get())
        quantidade = int(entry_qtd.get())

        if nome == "" or preco_compra <= 0 or preco_venda <= 0 or quantidade <= 0:
            messagebox.showerror("Erro", "Valores inválidos.")
            return

        custo = preco_compra * quantidade

        if custo > dinheiro:
            messagebox.showerror("Erro", "Dinheiro insuficiente.")
            return

        dinheiro -= custo
        compras_mes += custo
        compras_ano += custo

        produto = (proximo_id, nome, preco_compra, preco_venda, quantidade)
        produtos.append(produto)
        proximo_id += 1

        atualizar_status()
        listar_produtos()
        messagebox.showinfo("Sucesso", "Produto comprado!")

    except ValueError:
        messagebox.showerror("Erro", "Introduza valores numéricos válidos.")


def vender_produto():
    global dinheiro, vendas_mes, vendas_ano

    try:
        id_venda = int(entry_id_venda.get())
        quantidade_venda = int(entry_qtd_venda.get())

        if quantidade_venda <= 0:
            messagebox.showerror("Erro", "Quantidade inválida.")
            return

        for i, p in enumerate(produtos):
            if p[0] == id_venda:

                if quantidade_venda > p[4]:
                    messagebox.showerror("Erro", "Estoque insuficiente.")
                    return

                total = p[3] * quantidade_venda
                dinheiro += total
                vendas_mes += total
                vendas_ano += total

                nova_qtd = p[4] - quantidade_venda
                produtos[i] = (p[0], p[1], p[2], p[3], nova_qtd)

                atualizar_status()
                listar_produtos()
                messagebox.showinfo("Sucesso", "Venda realizada!")
                return

        messagebox.showerror("Erro", "Produto não encontrado.")

    except ValueError:
        messagebox.showerror("Erro", "Introduza valores válidos.")


def estatisticas_mes():
    lucro = vendas_mes - compras_mes
    messagebox.showinfo(
        "Estatísticas do Mês",
        f"Compras: {compras_mes:.2f}€\n"
        f"Vendas: {vendas_mes:.2f}€\n"
        f"Lucro: {lucro:.2f}€"
    )


def estatisticas_ano():
    lucro = vendas_ano - compras_ano
    messagebox.showinfo(
        "Estatísticas do Ano",
        f"Compras: {compras_ano:.2f}€\n"
        f"Vendas: {vendas_ano:.2f}€\n"
        f"Lucro: {lucro:.2f}€"
    )


def avancar_mes():
    global mes_atual, ano_atual, compras_mes, vendas_mes

    mes_atual += 1
    if mes_atual > 12:
        mes_atual = 1
        ano_atual += 1

    compras_mes = 0.0
    vendas_mes = 0.0

    atualizar_status()
    messagebox.showinfo("Tempo", "Mês avançado!")


# ==============================
# INTERFACE GRÁFICA
# ==============================

janela = tk.Tk()
janela.title("CEO da Empresa")
janela.geometry("800x600")

status_label = tk.Label(janela, text="", font=("Arial", 14))
status_label.pack(pady=10)

# ----- Comprar Produto -----
frame_compra = tk.LabelFrame(janela, text="Comprar Produto")
frame_compra.pack(fill="x", padx=10, pady=5)

tk.Label(frame_compra, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(frame_compra)
entry_nome.grid(row=0, column=1)

tk.Label(frame_compra, text="Preço Compra").grid(row=0, column=2)
entry_compra = tk.Entry(frame_compra)
entry_compra.grid(row=0, column=3)

tk.Label(frame_compra, text="Preço Venda").grid(row=0, column=4)
entry_venda = tk.Entry(frame_compra)
entry_venda.grid(row=0, column=5)

tk.Label(frame_compra, text="Quantidade").grid(row=0, column=6)
entry_qtd = tk.Entry(frame_compra)
entry_qtd.grid(row=0, column=7)

tk.Button(frame_compra, text="Comprar", command=comprar_produto).grid(row=0, column=8, padx=10)

# ----- Vender Produto -----
frame_venda = tk.LabelFrame(janela, text="Vender Produto")
frame_venda.pack(fill="x", padx=10, pady=5)

tk.Label(frame_venda, text="ID Produto").grid(row=0, column=0)
entry_id_venda = tk.Entry(frame_venda)
entry_id_venda.grid(row=0, column=1)

tk.Label(frame_venda, text="Quantidade").grid(row=0, column=2)
entry_qtd_venda = tk.Entry(frame_venda)
entry_qtd_venda.grid(row=0, column=3)

tk.Button(frame_venda, text="Vender", command=vender_produto).grid(row=0, column=4, padx=10)

# ----- Lista -----
lista = tk.Listbox(janela, width=100)
lista.pack(pady=10)

# ----- Botões Inferiores -----
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Estatísticas do Mês", command=estatisticas_mes).grid(row=0, column=0, padx=10)
tk.Button(frame_botoes, text="Estatísticas do Ano", command=estatisticas_ano).grid(row=0, column=1, padx=10)
tk.Button(frame_botoes, text="Avançar Mês", command=avancar_mes).grid(row=0, column=2, padx=10)

atualizar_status()
janela.mainloop()








