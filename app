# ==============================
# app.py
# interface grafica com tkinter
# substitui o menu terminal (main.py)
# importa as funcoes CRUD das entidades
# ==============================
import tkinter as tk
from tkinter import ttk, messagebox

from utilizadores import criar_utilizador, listar_utilizadores, consultar_utilizador, atualizar_utilizador, remover_utilizador
from jogos import criar_jogo, listar_jogos, consultar_jogo, atualizar_jogo, remover_jogo
from loja import criar_item_loja, listar_loja, consultar_item_loja, atualizar_item_loja, remover_item_loja
from compra import criar_compra, listar_compras, consultar_compra, atualizar_compra, remover_compra

# ── Cores e estilos ────────────────────────────────────────────────────────────
BG       = "#1a1a2e"
BG2      = "#16213e"
ACCENT   = "#0f6d6d"
ACCENT2  = "#2dd4bf"
FG       = "#e2e8f0"
FG_MUTED = "#94a3b8"
RED      = "#ef4444"
GREEN    = "#22c55e"
FONT     = ("Segoe UI", 10)
FONT_B   = ("Segoe UI", 10, "bold")
FONT_H   = ("Segoe UI", 14, "bold")


# ── Janela de formulário genérica ──────────────────────────────────────────────
class FormDialog(tk.Toplevel):
    def __init__(self, parent: tk.Widget, titulo, campos, callback, valores=None):
        # usa a janela raiz para centrar corretamente e evitar avisos de tipo
        root = parent.winfo_toplevel()
        super().__init__(root)
        self.title(titulo)
        self.configure(bg=BG2)
        self.resizable(False, False)
        self.grab_set()

        self.entries: dict[str, tk.Entry] = {}
        tk.Label(self, text=titulo, font=FONT_H, bg=BG2, fg=ACCENT2).pack(pady=(18, 10), padx=20)

        frame = tk.Frame(self, bg=BG2)
        frame.pack(padx=24, pady=4)

        for i, (campo, placeholder) in enumerate(campos):
            tk.Label(frame, text=campo, font=FONT_B, bg=BG2, fg=FG, anchor="w").grid(
                row=i, column=0, sticky="w", pady=4, padx=(0, 12))
            entry = tk.Entry(frame, font=FONT, bg=BG, fg=FG, insertbackground=FG,
                             relief="flat", bd=6, width=28)
            if valores and campo in valores and valores[campo]:
                entry.insert(0, valores[campo])
            else:
                entry.insert(0, placeholder)
                entry.config(fg=FG_MUTED)
                entry.bind("<FocusIn>",  lambda _, en=entry, ph=placeholder: self._clear(en, ph))
                entry.bind("<FocusOut>", lambda _, en=entry, ph=placeholder: self._restore(en, ph))
            entry.grid(row=i, column=1, pady=4)
            self.entries[campo] = entry

        btn_frame = tk.Frame(self, bg=BG2)
        btn_frame.pack(pady=16)
        tk.Button(btn_frame, text="Cancelar", font=FONT, bg=BG, fg=FG_MUTED,
                  relief="flat", bd=0, padx=16, pady=6,
                  command=self.destroy).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Confirmar", font=FONT_B, bg=ACCENT, fg="white",
                  relief="flat", bd=0, padx=16, pady=6,
                  command=lambda: callback(self)).pack(side="left", padx=6)

        self.update_idletasks()
        x = root.winfo_x() + (root.winfo_width()  - self.winfo_width())  // 2
        y = root.winfo_y() + (root.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    @staticmethod
    def _clear(entry: tk.Entry, placeholder: str):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(fg=FG)

    @staticmethod
    def _restore(entry: tk.Entry, placeholder: str):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg=FG_MUTED)


# ── Painel base para cada aba ──────────────────────────────────────────────────
class PainelBase(tk.Frame):
    def __init__(self, parent, colunas):
        super().__init__(parent, bg=BG)
        self.colunas = colunas
        self._build()

    def _build(self):
        btn_bar = tk.Frame(self, bg=BG, pady=10)
        btn_bar.pack(fill="x", padx=16)
        self._criar_botoes(btn_bar)

        frame_tree = tk.Frame(self, bg=BG2)
        frame_tree.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background=BG2, foreground=FG,
                        fieldbackground=BG2, rowheight=28,
                        font=FONT, borderwidth=0)
        style.configure("Treeview.Heading",
                        background=ACCENT, foreground="white",
                        font=FONT_B, relief="flat")
        style.map("Treeview", background=[("selected", ACCENT)])

        self.tree = ttk.Treeview(frame_tree, columns=self.colunas,
                                 show="headings", selectmode="browse")
        for col in self.colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=130)

        scroll = ttk.Scrollbar(frame_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.tree.tag_configure("odd",  background="#1c2b3a")
        self.tree.tag_configure("even", background=BG2)

        self.carregar_lista()

    @staticmethod
    def _btn(parent: tk.Frame, texto: str, cor: str, comando):
        tk.Button(parent, text=texto, font=FONT_B, bg=cor, fg="white",
                  relief="flat", bd=0, padx=14, pady=6,
                  cursor="hand2", command=comando).pack(side="left", padx=4)

    def _criar_botoes(self, bar):
        pass

    def carregar_lista(self):
        pass

    def _refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.carregar_lista()

    def _selecionado_id(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Aviso", "Seleciona um registo primeiro.", parent=self)
            return None
        return self.tree.item(sel)["values"][0]


# ══════════════════════════════════════════════════════════════════════════════
# ABA — UTILIZADORES
# ══════════════════════════════════════════════════════════════════════════════
class PainelUtilizadores(PainelBase):
    def __init__(self, parent):
        super().__init__(parent, ("ID", "Nome", "Username", "Email", "Nascimento"))

    def _criar_botoes(self, bar):
        self._btn(bar, "+ Criar",   GREEN,  self.criar)
        self._btn(bar, "✎ Editar",  ACCENT, self.editar)
        self._btn(bar, "✕ Remover", RED,    self.remover)
        tk.Button(bar, text="↺ Atualizar", font=FONT, bg=BG2, fg=FG_MUTED,
                  relief="flat", bd=0, padx=10, pady=6,
                  command=self._refresh).pack(side="right", padx=4)

    def carregar_lista(self):
        code, obj = listar_utilizadores()
        if code == 200:
            for i, (uid, d) in enumerate(obj.items()):
                tag = "odd" if i % 2 else "even"
                self.tree.insert("", "end",
                    values=(uid, d["nome"], d["username"], d["email"], d["nascimento"]),
                    tags=(tag,))

    def criar(self):
        campos = [("Nome", ""), ("Username", ""), ("Email", ""),
                  ("Password", ""), ("Nascimento (DD-MM-AAAA)", "")]
        def confirmar(dialog):
            code, obj = criar_utilizador(
                dialog.entries["Nome"].get(),
                dialog.entries["Username"].get(),
                dialog.entries["Email"].get(),
                dialog.entries["Password"].get(),
                dialog.entries["Nascimento (DD-MM-AAAA)"].get()
            )
            if code == 201:
                messagebox.showinfo("Sucesso", f"Utilizador criado! ID: {obj['uid']}", parent=dialog)
                dialog.destroy(); self._refresh()
            else:
                messagebox.showerror("Erro", obj, parent=dialog)
        FormDialog(self, "Criar Utilizador", campos, confirmar)

    def editar(self):
        uid = self._selecionado_id()
        if not uid: return
        code, d = consultar_utilizador(str(uid))
        if code != 200:
            messagebox.showerror("Erro", d, parent=self); return
        campos = [("Nome", ""), ("Username", ""), ("Email", ""),
                  ("Password", ""), ("Nascimento (DD-MM-AAAA)", "")]
        valores = {"Nome": d["nome"], "Username": d["username"],
                   "Email": d["email"], "Nascimento (DD-MM-AAAA)": d["nascimento"]}
        def confirmar(dialog):
            code2, obj = atualizar_utilizador(
                str(uid),
                dialog.entries["Nome"].get() or None,
                dialog.entries["Username"].get() or None,
                dialog.entries["Email"].get() or None,
                dialog.entries["Password"].get() or None,
                dialog.entries["Nascimento (DD-MM-AAAA)"].get() or None
            )
            if code2 == 200:
                messagebox.showinfo("Sucesso", "Utilizador atualizado!", parent=dialog)
                dialog.destroy(); self._refresh()
            else:
                messagebox.showerror("Erro", obj, parent=dialog)
        FormDialog(self, "Editar Utilizador", campos, confirmar, valores)

    def remover(self):
        uid = self._selecionado_id()
        if not uid: return
        if not messagebox.askyesno("Confirmar", f"Remover utilizador {uid}?", parent=self): return
        code, obj = remover_utilizador(str(uid))
        if code == 200:
            messagebox.showinfo("Sucesso", f"Utilizador {uid} removido.", parent=self)
            self._refresh()
        else:
            messagebox.showerror("Erro", obj, parent=self)


# ══════════════════════════════════════════════════════════════════════════════
# ABA — JOGOS
# ══════════════════════════════════════════════════════════════════════════════
class PainelJogos(PainelBase):
    def __init__(self, parent):
        super().__init__(parent, ("ID", "Nome", "Modo", "Idade Mínima", "Tamanho (GB)"))

    def _criar_botoes(self, bar):
        self._btn(bar, "+ Criar",   GREEN,  self.criar)
        self._btn(bar, "✎ Editar",  ACCENT, self.editar)
        self._btn(bar, "✕ Remover", RED,    self.remover)
        tk.Button(bar, text="↺ Atualizar", font=FONT, bg=BG2, fg=FG_MUTED,
                  relief="flat", bd=0, padx=10, pady=6,
                  command=self._refresh).pack(side="right", padx=4)

    def carregar_lista(self):
        code, obj = listar_jogos()
        if code == 200:
            for i, (jid, d) in enumerate(obj.items()):
                tag = "odd" if i % 2 else "even"
                self.tree.insert("", "end",
                    values=(jid, d["nome"], d["modo"], d["idade_minima"], d["tamanho_gb"]),
                    tags=(tag,))

    def criar(self):
        campos = [("Nome", ""), ("Modo (single player/multiplayer/ambos)", ""),
                  ("Idade Mínima", ""), ("Tamanho GB", "")]
        def confirmar(dialog):
            code, obj = criar_jogo(
                dialog.entries["Nome"].get(),
                dialog.entries["Modo (single player/multiplayer/ambos)"].get(),
                dialog.entries["Idade Mínima"].get(),
                dialog.entries["Tamanho GB"].get()
            )
            if code == 201:
                messagebox.showinfo("Sucesso", "Jogo criado!", parent=dialog)
                dialog.destroy(); self._refresh()
            else:
                messagebox.showerror("Erro", obj, parent=dialog)
        FormDialog(self, "Criar Jogo", campos, confirmar)

    def editar(self):
        jid = self._selecionado_id()
        if not jid: return
        code, d = consultar_jogo(str(jid))
        if code != 200:
            messagebox.showerror("Erro", d, parent=self); return
        campos = [("Nome", ""), ("Modo (single player/multiplayer/ambos)", ""),
                  ("Idade Mínima", ""), ("Tamanho GB", "")]
        valores = {"Nome": d["nome"],
                   "Modo (single player/multiplayer/ambos)": d["modo"],
                   "Idade Mínima": str(d["idade_minima"]),
                   "Tamanho GB": str(d["tamanho_gb"])}
        def confirmar(dialog):
            code2, obj = atualizar_jogo(
                str(jid),
                dialog.entries["Nome"].get() or None,
                dialog.entries["Modo (single player/multiplayer/ambos)"].get() or None,
                dialog.entries["Idade Mínima"].get() or None,
                dialog.entries["Tamanho GB"].get() or None
            )
            if code2 == 200:
                messagebox.showinfo("Sucesso", "Jogo atualizado!", parent=dialog)
                dialog.destroy(); self._refresh()
            else:
                messagebox.showerror("Erro", obj, parent=dialog)
        FormDialog(self, "Editar Jogo", campos, confirmar, valores)

    def remover(self):
        jid = self._selecionado_id()
        if not jid: return
        if not messagebox.askyesno("Confirmar", f"Remover jogo {jid}?", parent=self): return
        code, obj = remover_jogo(str(jid))
        if code == 200:
            messagebox.showinfo("Sucesso", f"Jogo {jid} removido.", parent=self)
            self._refresh()
        else:
            messagebox.showerror("Erro", obj, parent=self)


# ══════════════════════════════════════════════════════════════════════════════
# ABA — LOJA
# ══════════════════════════════════════════════════════════════════════════════
class PainelLoja(PainelBase):
    def __init__(self, parent):
        super().__init__(parent, ("ID", "Jogo", "Preço (€)", "Stock"))

    def _criar_botoes(self, bar):
        self._btn(bar, "+ Adicionar", GREEN,  self.criar)
        self._btn(bar, "✎ Editar",    ACCENT, self.editar)
        self._btn(bar, "✕ Remover",   RED,    self.remover)
        tk.Button(bar, text="↺ Atualizar", font=FONT, bg=BG2, fg=FG_MUTED,
                  relief="flat", bd=0, padx=10, pady=6,
                  command=self._refresh).pack(side="right", padx=4)

    def carregar_lista(self):
        code, obj = listar_loja()
        if code == 200:
            from jogos import jogos
            for i, (lid, d) in enumerate(obj.items()):
                nome_jogo = jogos[d["jid"]]["nome"] if d["jid"] in jogos else "Jogo removido"
                tag = "odd" if i % 2 else "even"
                self.tree.insert("", "end",
                    values=(lid, nome_jogo, f"{d['preco']:.2f}", d["stock"]),
                    tags=(tag,))

    def criar(self):
        campos = [("ID do Jogo", ""), ("Preço (€)", ""), ("Stock", "")]
        def confirmar(dialog):
            code, obj = criar_item_loja(
                dialog.entries["ID do Jogo"].get(),
                dialog.entries["Preço (€)"].get(),
                dialog.entries["Stock"].get()
            )
            if code == 201:
                messagebox.showinfo("Sucesso", f"Item adicionado à loja! ID: {obj}", parent=dialog)
                dialog.destroy(); self._refresh()
            else:
                messagebox.showerror("Erro", obj, parent=dialog)
        FormDialog(self, "Adicionar à Loja", campos, confirmar)

    def editar(self):
        lid = self._selecionado_id()
        if not lid: return
        code, d = consultar_item_loja(str(lid))
        if code != 200:
            messagebox.showerror("Erro", d, parent=self); return
        campos = [("Preço (€)", ""), ("Stock", "")]
        valores = {"Preço (€)": str(d["preco"]), "Stock": str(d["stock"])}
        def confirmar(dialog):
            code2, obj = atualizar_item_loja(
                str(lid),
                dialog.entries["Preço (€)"].get() or None,
                dialog.entries["Stock"].get() or None
            )
            if code2 == 200:
                messagebox.showinfo("Sucesso", "Item atualizado!", parent=dialog)
                dialog.destroy(); self._refresh()
            else:
                messagebox.showerror("Erro", obj, parent=dialog)
        FormDialog(self, "Editar Item da Loja", campos, confirmar, valores)

    def remover(self):
        lid = self._selecionado_id()
        if not lid: return
        if not messagebox.askyesno("Confirmar", f"Remover item {lid} da loja?", parent=self): return
        code, obj = remover_item_loja(str(lid))
        if code == 200:
            messagebox.showinfo("Sucesso", f"Item {lid} removido.", parent=self)
            self._refresh()
        else:
            messagebox.showerror("Erro", obj, parent=self)


# ══════════════════════════════════════════════════════════════════════════════
# ABA — COMPRAS
# ══════════════════════════════════════════════════════════════════════════════
class PainelCompras(PainelBase):
    def __init__(self, parent):
        super().__init__(parent, ("ID", "Utilizador", "Item Loja", "Data", "Preço Pago (€)"))

    def _criar_botoes(self, bar):
        self._btn(bar, "+ Registar", GREEN,  self.criar)
        self._btn(bar, "✎ Editar",   ACCENT, self.editar)
        self._btn(bar, "✕ Cancelar", RED,    self.remover)
        tk.Button(bar, text="↺ Atualizar", font=FONT, bg=BG2, fg=FG_MUTED,
                  relief="flat", bd=0, padx=10, pady=6,
                  command=self._refresh).pack(side="right", padx=4)

    def carregar_lista(self):
        code, obj = listar_compras()
        if code == 200:
            for i, (cid, d) in enumerate(obj.items()):
                tag = "odd" if i % 2 else "even"
                self.tree.insert("", "end",
                    values=(cid, d["uid"], d["lid"], d["data_compra"], f"{d['preco_pago']:.2f}"),
                    tags=(tag,))

    def criar(self):
        campos = [("ID do Utilizador", ""), ("ID do Item da Loja", ""), ("Data (DD-MM-AAAA)", "")]
        def confirmar(dialog):
            code, obj = criar_compra(
                dialog.entries["ID do Utilizador"].get(),
                dialog.entries["ID do Item da Loja"].get(),
                dialog.entries["Data (DD-MM-AAAA)"].get()
            )
            if code == 201:
                messagebox.showinfo("Sucesso", f"Compra registada! ID: {obj}", parent=dialog)
                dialog.destroy(); self._refresh()
            else:
                messagebox.showerror("Erro", obj, parent=dialog)
        FormDialog(self, "Registar Compra", campos, confirmar)

    def editar(self):
        cid = self._selecionado_id()
        if not cid: return
        code, d = consultar_compra(str(cid))
        if code != 200:
            messagebox.showerror("Erro", d, parent=self); return
        campos = [("Nova Data (DD-MM-AAAA)", "")]
        valores = {"Nova Data (DD-MM-AAAA)": d["data_compra"]}
        def confirmar(dialog):
            code2, obj = atualizar_compra(
                str(cid),
                dialog.entries["Nova Data (DD-MM-AAAA)"].get() or None
            )
            if code2 == 200:
                messagebox.showinfo("Sucesso", "Compra atualizada!", parent=dialog)
                dialog.destroy(); self._refresh()
            else:
                messagebox.showerror("Erro", obj, parent=dialog)
        FormDialog(self, "Editar Compra", campos, confirmar, valores)

    def remover(self):
        cid = self._selecionado_id()
        if not cid: return
        if not messagebox.askyesno("Confirmar", f"Cancelar compra {cid}? O stock será devolvido.", parent=self): return
        code, obj = remover_compra(str(cid))
        if code == 200:
            messagebox.showinfo("Sucesso", f"Compra {cid} cancelada. Stock devolvido.", parent=self)
            self._refresh()
        else:
            messagebox.showerror("Erro", obj, parent=self)


# ══════════════════════════════════════════════════════════════════════════════
# JANELA PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎮 Gestor de Steam")
        self.geometry("900x580")
        self.minsize(800, 500)
        self.configure(bg=BG)
        self._build()

    def _build(self):
        header = tk.Frame(self, bg=ACCENT, height=52)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="🎮  GESTOR DE STEAM",
                 font=("Segoe UI", 14, "bold"), bg=ACCENT, fg="white").pack(side="left", padx=20)

        style = ttk.Style()
        style.configure("TNotebook",      background=BG, borderwidth=0)
        style.configure("TNotebook.Tab",  background=BG2, foreground=FG_MUTED,
                                          font=FONT_B, padding=(16, 8))
        style.map("TNotebook.Tab",
                  background=[("selected", ACCENT)],
                  foreground=[("selected", "white")])

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True)

        nb.add(PainelUtilizadores(nb), text="  👤 Utilizadores  ")
        nb.add(PainelJogos(nb),        text="  🎮 Jogos  ")
        nb.add(PainelLoja(nb),         text="  🏪 Loja  ")
        nb.add(PainelCompras(nb),      text="  🛒 Compras  ")


# ── ponto de entrada ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    App().mainloop()


    
