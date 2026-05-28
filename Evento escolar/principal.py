import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from funcoes import contar_por_atividade, limpar_campos, atualizar_visualizacao


# ================================
#        DADOS DO SISTEMA
# ================================

participantes = []  # LISTA de TUPLOS

emails_registados = set()  # SET de strings

#ordem crescente
atividades_base = sorted([
    "Xadrez", "Futebol", "Basquetebol", "Andebol",
    "Paintball", "Ping Pong", "Dança", "Kitesurf",
    "E-Sports Pro", "Escalada Radical"
])  # LISTA de strings

# máximo de participantes por atividade
limite_por_atividade = 5


# ================================
#          FUNÇÕES LÓGICAS
# ================================

def atualizar_combo():
    """
    Atualiza a combobox de atividades.
    Mostra apenas atividades que ainda não atingiram o limite de participantes.
    """


    atividades_formatadas = []  # LISTA de strings

    for atividade in atividades_base:
        # conta quantos participantes já existem nesta atividade
        total = contar_por_atividade(atividade, participantes)

        # Só adiciona à lista se ainda houver vagas
        if total < limite_por_atividade:
            # Formata o texto para mostrar quantidade de inscritos e limite
            atividades_formatadas.append(
                f"{atividade} ({total}/{limite_por_atividade})"
            )

    # Atualiza a combobox com os valores disponíveis
    combo['values'] = atividades_formatadas
    combo.set("Selecione...")  # valor inicial padrão


def registar():
    """
    Função responsável por validar e registar
    um novo participante.
    """
    #pega, remove, guarda na variavel
    nome = ent_nome.get().strip()
    email = ent_email.get().strip()
    atividade_formatada = combo.get()  # texto selecionado na combobox

    # Validação do nome (números e vazio)
    if any(char.isdigit() for char in nome) or not nome:
        messagebox.showerror("Erro", "Nome deve conter apenas letras.")
        return

    # Validação do email
    if "@" not in email:
        messagebox.showerror("Erro", "Formato de email inválido.")
        return

    # Verifica se foi escolhida uma atividade válida
    if atividade_formatada == "Selecione...":
        messagebox.showwarning("Aviso", "Escolha uma atividade.")
        return

    # Verifica se o email já foi registado (set garante unicidade)
    if email in emails_registados:
        messagebox.showwarning("Aviso", "Este email já está registado.")
        return

    # Extrai apenas o nome da atividade (remove o contador 0/5 etc)
    atividade = atividade_formatada.split(" (")[0]

    # Verifica se a atividade já atingiu o limite
    if contar_por_atividade(atividade, participantes) >= limite_por_atividade:
        messagebox.showwarning("Limite atingido",
                               "Esta atividade já tem 5 participantes.")
        return
    #tuplo para participante
    participante = (nome, email, atividade)  # TUPLO

    #adiciona tuplo a lista
    participantes.append(participante)  # LISTA de TUPLOS

    # Adiciona email ao set para evitar duplicações
    emails_registados.add(email)  # SET

    # Atualiza a interface: listbox, contador, combobox
    atualizar_visualizacao(participantes, listbox, ent_filtro, atividades_base, lbl_contador, tk)
    atualizar_combo()
    limpar_campos(ent_nome, ent_email, tk, combo)

    messagebox.showinfo("Sucesso", f"Inscrição de {nome} realizada!")


def anular():
    """
    Remove um participante selecionado na listbox.
    Pede confirmação antes de apagar.
    """
    try:
        selecao = listbox.get(listbox.curselection())

        # Evita apagar títulos de atividade (ex: === Basquetebol ===)
        if "===" in selecao:
            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            "Tem a certeza que deseja remover este participante?"
        )

        if not confirmar:
            return

        # Procura participante pelo email contido na seleção
        for i, p in enumerate(participantes):  # LISTA de TUPLOS
            if p[1] in selecao:
                # Remove o email
                emails_registados.remove(p[1])  # SET
                # Remove o tuplo
                participantes.pop(i)  # LISTA
                break

        # Atualiza a interface novamente
        atualizar_visualizacao(participantes, listbox, ent_filtro, atividades_base, lbl_contador, tk)
        atualizar_combo()

    except:
        messagebox.showwarning("Aviso",
                               "Selecione um participante válido.")


# ================================
#          INTERFACE GRÁFICA
# ================================

root = tk.Tk()
root.title("SGE 2026 - Gestão de Participantes")
root.geometry("650x750")
root.configure(bg="#0f172a")

style = ttk.Style()
style.theme_use('clam')

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

aba_registo = tk.Frame(notebook, bg="#1e293b")
aba_lista = tk.Frame(notebook, bg="#1e293b")

notebook.add(aba_registo, text="  📝 Novo Registo  ")
notebook.add(aba_lista, text="  🔍 Consultar / Filtrar  ")

# --------------------------
# ABA DE REGISTO
# --------------------------
tk.Label(aba_registo, text="FORMULÁRIO DE INSCRIÇÃO",
         font=('Arial', 14, 'bold'),
         fg="#38bdf8", bg="#1e293b").pack(pady=30)

container = tk.Frame(aba_registo, bg="#1e293b")
container.pack(pady=10)

tk.Label(container, text="Nome do Aluno:",
         fg="white", bg="#1e293b").grid(row=0, column=0, sticky="w", pady=10)
ent_nome = tk.Entry(container, width=35, font=('Arial', 11))
ent_nome.grid(row=0, column=1, padx=10)

tk.Label(container, text="Email Institucional:",
         fg="white", bg="#1e293b").grid(row=1, column=0, sticky="w", pady=10)
ent_email = tk.Entry(container, width=35, font=('Arial', 11))
ent_email.grid(row=1, column=1, padx=10)

tk.Label(container, text="Atividade Pretendida:",
         fg="white", bg="#1e293b").grid(row=2, column=0, sticky="w", pady=10)

combo = ttk.Combobox(container, state="readonly",
                     width=33, font=('Arial', 10))
combo.grid(row=2, column=1, padx=10)

atualizar_combo()

tk.Button(aba_registo, text="CONCLUIR REGISTO",
          command=registar,
          bg="#10b981", fg="white",
          font=('Arial', 11, 'bold'),
          width=30, pady=10, bd=0).pack(pady=40)


# --------------------------
# ABA DE CONSULTA
# --------------------------
f_topo = tk.Frame(aba_lista, bg="#334155", pady=15)
f_topo.pack(fill="x")

tk.Label(f_topo, text="Filtrar por Atividade ou Email:",
         fg="white", bg="#334155").pack()

ent_filtro = tk.Entry(f_topo, width=50, font=('Arial', 11))
ent_filtro.pack(pady=5)

# Atualiza automaticamente a listbox ao digitar
ent_filtro.bind("<KeyRelease>", lambda e: atualizar_visualizacao(
    participantes, listbox, ent_filtro, atividades_base, lbl_contador, tk))

f_lista = tk.Frame(aba_lista, bg="#1e293b")
f_lista.pack(fill="both", expand=True, padx=20, pady=10)

listbox = tk.Listbox(f_lista, bg="#0f172a",
                     fg="#f8fafc",
                     font=('Consolas', 11), bd=0)
listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(f_lista)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

lbl_contador = tk.Label(aba_lista,
                        text="Total de inscritos: 0",
                        fg="#94a3b8", bg="#1e293b")
lbl_contador.pack(pady=5)

tk.Button(aba_lista,
          text="Anular Inscrição Selecionada",
          command=anular,
          bg="#ef4444", fg="white",
          font=('Arial', 10)).pack(pady=10)

if __name__ == "__main__":
    root.mainloop()