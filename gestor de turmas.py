import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import json
import os

FICHEIRO = "turma.json"

alunos = {}

# =========================
# DADOS
# =========================

def guardar():
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)
    messagebox.showinfo("Sucesso", "Dados guardados")

def carregar():
    global alunos
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            alunos = json.load(f)

# =========================
# FUNÇÕES
# =========================

def atualizar_lista():
    tree.delete(*tree.get_children())
    for id_aluno, a in alunos.items():
        media = calcular_media(a["notas"])
        tree.insert(
            "", "end",
            values=(
                id_aluno,
                a["nome"],
                media,
                len(a["faltas_presenca"]),
                len(a["faltas_material"])
            )
        )

def calcular_media(notas):
    medias = []
    for n in notas.values():
        if n:
            medias.append(sum(n) / len(n))
    return round(sum(medias) / len(medias), 2) if medias else 0.0

def adicionar_aluno():
    try:
        id_aluno = entry_id.get()
        nome = entry_nome.get()

        alunos[id_aluno] = {
            "nome": nome,
            "notas": {},
            "faltas_presenca": [],
            "faltas_material": []
        }

        entry_id.delete(0, tk.END)
        entry_nome.delete(0, tk.END)
        atualizar_lista()
    except:
        messagebox.showerror("Erro", "Dados inválidos")

def aluno_selecionado():
    sel = tree.focus()
    if not sel:
        return None
    return tree.item(sel)["values"][0]

def remover_aluno():
    id_aluno = aluno_selecionado()
    if not id_aluno:
        return

    nome = alunos[id_aluno]["nome"]

    confirmar = messagebox.askyesno(
        "Confirmar remoção",
        f"Tens a certeza que queres remover o aluno '{nome}'?"
    )

    if confirmar:
        del alunos[id_aluno]
        atualizar_lista()

def lancar_nota():
    id_aluno = aluno_selecionado()
    if not id_aluno:
        return

    w = tk.Toplevel(root)
    w.title("Lançar Nota")
    w.geometry("300x200")

    tk.Label(w, text="Disciplina").pack(pady=5)
    e_disc = tk.Entry(w)
    e_disc.pack(pady=5)

    tk.Label(w, text="Nota").pack(pady=5)
    e_nota = tk.Entry(w)
    e_nota.pack(pady=5)

    def guardar_nota():
        try:
            alunos[id_aluno]["notas"].setdefault(e_disc.get(), []).append(float(e_nota.get()))
            atualizar_lista()
            w.destroy()
        except:
            messagebox.showerror("Erro", "Nota inválida")

    tk.Button(w, text="Guardar", command=guardar_nota).pack(pady=10)

def falta_presenca():
    id_aluno = aluno_selecionado()
    if id_aluno:
        alunos[id_aluno]["faltas_presenca"].append(str(date.today()))
        atualizar_lista()

def falta_material():
    id_aluno = aluno_selecionado()
    if id_aluno:
        alunos[id_aluno]["faltas_material"].append(str(date.today()))
        atualizar_lista()

# =========================
# INTERFACE
# =========================

root = tk.Tk()
root.title("Gestão de Turma")
root.geometry("900x600")

carregar()

tk.Label(root, text="Sistema de Gestão de Turma", font=("Arial", 20, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=20)

left = tk.Frame(frame)
left.pack(side="left", fill="y", padx=10)

tk.Label(left, text="ID").pack()
entry_id = tk.Entry(left)
entry_id.pack(pady=5)

tk.Label(left, text="Nome").pack()
entry_nome = tk.Entry(left)
entry_nome.pack(pady=5)

tk.Button(left, text="Adicionar Aluno", command=adicionar_aluno).pack(pady=10)
tk.Button(left, text="Guardar", command=guardar).pack(pady=10)

right = tk.Frame(frame)
right.pack(side="right", fill="both", expand=True)

cols = ("ID", "Nome", "Média", "F. Presença", "F. Material")
tree = ttk.Treeview(right, columns=cols, show="headings")

for c in cols:
    tree.heading(c, text=c)
    tree.column(c, anchor="center")

tree.pack(fill="both", expand=True, pady=10)

btns = tk.Frame(right)
btns.pack(pady=10)

tk.Button(btns, text="Lançar Nota", command=lancar_nota).grid(row=0, column=0, padx=5)
tk.Button(btns, text="Falta Presença", command=falta_presenca).grid(row=0, column=1, padx=5)
tk.Button(btns, text="Falta Material", command=falta_material).grid(row=0, column=2, padx=5)
tk.Button(btns, text="Remover", command=remover_aluno).grid(row=0, column=3, padx=5)

atualizar_lista()
root.mainloop()




