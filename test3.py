import tkinter as tk
from tkinter import font as tkfont
import random

# ── Paleta ────────────────────────────────────────────────────────
BG       = "#07090f"
PANEL    = "#0d1117"
BORDER   = "#1e3a2f"
GREEN    = "#00ff88"
GREEN2   = "#00cc66"
RED      = "#ff3355"
YELLOW   = "#ffcc00"
BLUE     = "#00aaff"
TEXT     = "#c8ffd4"
MUTED    = "#4a7a5a"
WHITE    = "#e8fff0"

# ── Perguntas ─────────────────────────────────────────────────────
QUESTIONS = [
    {
        "diff": "MÉDIO",
        "text": "O que afirma a Lei da Conservação das Massas (Lei de Lavoisier)?",
        "opts": [
            "A energia não pode ser criada nem destruída",
            "A massa total dos reagentes é igual à massa total dos produtos numa reação química",
            "Todo elemento tem uma massa atómica fixa",
            "Num composto, os elementos combinam-se em proporções variáveis"
        ],
        "ans": 1,
        "exp": "Lavoisier (1774): \"Na natureza nada se cria, nada se perde, tudo se transforma.\"\nMassa reagentes = massa produtos. É a base de toda a estequiometria."
    },
    {
        "diff": "FÁCIL",
        "text": "Numa reação química, misturaram-se 20 g de reagente A com 30 g de reagente B num recipiente fechado. Qual é a massa total dos produtos formados?",
        "opts": ["20 g", "30 g", "50 g", "10 g"],
        "ans": 2,
        "exp": "Pela Lei de Lavoisier: massa reagentes = massa produtos.\n20 g + 30 g = 50 g. Em sistema fechado, a massa é sempre conservada."
    },
    {
        "diff": "MÉDIO",
        "text": "Um estudante queima magnésio (Mg) ao ar e vê que o produto MgO tem massa MAIOR que o Mg inicial. Isso contradiz Lavoisier?",
        "opts": [
            "Sim, porque a massa aumentou",
            "Não, porque o oxigênio do ar também é reagente e deve ser incluído na massa total",
            "Sim, mas apenas para metais",
            "Não, porque Lavoisier só se aplica a líquidos"
        ],
        "ans": 1,
        "exp": "Não contradiz! O oxigênio do ar é reagente.\nMassa Mg + massa O₂ consumido = massa MgO.\nA lei vale para TODOS os reagentes, incluindo gases do ar."
    },
    {
        "diff": "MÉDIO",
        "text": "Qual das frases seguintes descreve corretamente uma reação química?",
        "opts": [
            "Os átomos são destruídos e novos são criados",
            "Os átomos reorganizam-se formando novas substâncias, mas a quantidade total de átomos mantém-se",
            "A massa dos produtos é sempre menor que a dos reagentes",
            "Apenas ocorre em laboratório, nunca na natureza"
        ],
        "ans": 1,
        "exp": "Numa reação química os átomos não se criam nem destroem — apenas se reorganizam.\nÉ por isso que a massa total é conservada (Lavoisier)."
    },
    {
        "diff": "FÁCIL",
        "text": "A reação  H₂ + Cl₂ → 2HCl  é um exemplo de que tipo de reação?",
        "opts": ["Decomposição", "Síntese (combinação)", "Dupla troca", "Combustão"],
        "ans": 1,
        "exp": "É uma reação de SÍNTESE: dois ou mais reagentes combinam-se para formar um único produto.\nAqui H₂ e Cl₂ formam HCl (ácido clorídrico)."
    },
    {
        "diff": "FÁCIL",
        "text": "Na reação  2H₂O → 2H₂ + O₂  (eletrólise da água), qual é o tipo de reação?",
        "opts": ["Síntese", "Decomposição", "Simples troca", "Dupla troca"],
        "ans": 1,
        "exp": "É uma DECOMPOSIÇÃO (análise): um único reagente divide-se em dois ou mais produtos.\nA água é separada nos seus elementos por ação da corrente elétrica."
    },
    {
        "diff": "MÉDIO",
        "text": "Qual das seguintes reações é uma reação de simples troca (deslocamento)?",
        "opts": [
            "NaOH + HCl → NaCl + H₂O",
            "Fe + CuSO₄ → FeSO₄ + Cu",
            "CaCO₃ → CaO + CO₂",
            "H₂ + O₂ → H₂O"
        ],
        "ans": 1,
        "exp": "Fe + CuSO₄ → FeSO₄ + Cu é simples troca:\no ferro (mais reativo) desloca o cobre do seu sal."
    },
    {
        "diff": "MÉDIO",
        "text": "A reação  HCl + NaOH → NaCl + H₂O  é uma neutralização. Como se classifica?",
        "opts": ["Síntese", "Decomposição", "Simples troca", "Dupla troca (neutralização)"],
        "ans": 3,
        "exp": "É uma DUPLA TROCA — especificamente uma neutralização ácido-base.\nOs iões H⁺ do ácido e OH⁻ da base formam água. Os outros iões formam o sal NaCl."
    },
    {
        "diff": "FÁCIL",
        "text": "Porque é necessário balancear uma equação química?",
        "opts": [
            "Para a equação ficar mais bonita",
            "Para respeitar a Lei de Lavoisier — o nº de átomos de cada elemento deve ser igual nos dois lados",
            "Para facilitar a leitura dos símbolos",
            "Porque é uma regra apenas estética"
        ],
        "ans": 1,
        "exp": "Balancear é respeitar a Lei de Lavoisier.\nO número de átomos de cada elemento tem de ser igual nos reagentes e nos produtos."
    },
    {
        "diff": "MÉDIO",
        "text": "Qual é o coeficiente correto do O₂ na combustão do hidrogênio?\n2H₂ + _O₂ → 2H₂O",
        "opts": ["1", "2", "3", "4"],
        "ans": 0,
        "exp": "2H₂ + O₂ → 2H₂O\nH = 4 (esq.) = 4 (dir.) ✓\nO = 2 (esq.) = 2 (dir.) ✓\nO coeficiente do O₂ é 1."
    },
    {
        "diff": "MÉDIO",
        "text": "Verifica qual equação está corretamente balanceada:",
        "opts": [
            "H₂ + O₂ → H₂O",
            "2H₂ + O₂ → 2H₂O",
            "H₂ + 2O₂ → H₂O",
            "H₂ + O → H₂O"
        ],
        "ans": 1,
        "exp": "2H₂ + O₂ → 2H₂O é a única balanceada:\nH=4=4 ✓  e  O=2=2 ✓\nAs outras violam a Lei de Lavoisier."
    },
    {
        "diff": "FÁCIL",
        "text": "O que são reagentes numa equação química?",
        "opts": [
            "As substâncias formadas no final da reação",
            "As substâncias que existem antes da reação e que se transformam",
            "Os símbolos escritos do lado direito da seta",
            "Os catalisadores usados na reação"
        ],
        "ans": 1,
        "exp": "Os REAGENTES são as substâncias de partida, escritas à ESQUERDA da seta (→).\nOs PRODUTOS são o que se forma, escritos à direita."
    },
    {
        "diff": "FÁCIL",
        "text": "Qual dos seguintes é um exemplo de reação química do quotidiano?",
        "opts": [
            "Derreter gelo para obter água",
            "Dissolver açúcar no café",
            "Queimar uma vela",
            "Partir um copo de vidro"
        ],
        "ans": 2,
        "exp": "Queimar uma vela é uma reação química (combustão):\na parafina reage com O₂ produzindo CO₂ e H₂O.\nAs outras opções são mudanças físicas."
    },
    {
        "diff": "MÉDIO",
        "text": "Ao misturar carbonato de cálcio (CaCO₃) com ácido clorídrico (HCl) observa-se libertação de gás. Qual é esse gás?\nCaCO₃ + 2HCl → CaCl₂ + H₂O + ?",
        "opts": ["Oxigênio (O₂)", "Hidrogênio (H₂)", "Dióxido de carbono (CO₂)", "Cloro (Cl₂)"],
        "ans": 2,
        "exp": "CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂↑\nO dióxido de carbono libertado provoca efervescência visível.\nEste teste serve para identificar carbonatos."
    },
    {
        "diff": "MÉDIO",
        "text": "A massa dos reagentes numa reação em sistema fechado é 85 g.\nUm dos produtos tem massa 60 g. Qual é a massa do outro produto?",
        "opts": ["60 g", "25 g", "145 g", "85 g"],
        "ans": 1,
        "exp": "Pela Lei de Lavoisier: massa total produtos = 85 g.\nProduto 1 = 60 g\nProduto 2 = 85 − 60 = 25 g\nA soma dos produtos é sempre igual à soma dos reagentes."
    },
]

# ── Estado global ─────────────────────────────────────────────────
questions = []
qi = 0
correct = 0
wrong = 0
streak = 0
max_streak = 0
answered = False
option_buttons = []

# ══════════════════════════════════════════════════════════════════
# JANELA PRINCIPAL
# ══════════════════════════════════════════════════════════════════
janela = tk.Tk()
janela.title("⚗ Quiz de Química — 10.º Ano")
janela.geometry("820x660")
janela.configure(bg=BG)
janela.resizable(False, False)

# ── Fontes ────────────────────────────────────────────────────────
f_title   = tkfont.Font(family="Courier New", size=16, weight="bold")
f_sub     = tkfont.Font(family="Courier New", size=9)
f_score   = tkfont.Font(family="Courier New", size=10, weight="bold")
f_score_v = tkfont.Font(family="Courier New", size=18, weight="bold")
f_meta    = tkfont.Font(family="Courier New", size=9)
f_q       = tkfont.Font(family="Courier New", size=11)
f_opt     = tkfont.Font(family="Courier New", size=10)
f_exp     = tkfont.Font(family="Courier New", size=10)
f_btn     = tkfont.Font(family="Courier New", size=11, weight="bold")
f_result  = tkfont.Font(family="Courier New", size=16, weight="bold")
f_pct     = tkfont.Font(family="Courier New", size=34, weight="bold")

# ══════════════════════════════════════════════════════════════════
# LAYOUT
# ══════════════════════════════════════════════════════════════════

# ── Cabeçalho ─────────────────────────────────────────────────────
frame_header = tk.Frame(janela, bg=BG)
frame_header.pack(fill="x", pady=(10, 2))

tk.Label(frame_header, text="⚗  LABORATÓRIO VIRTUAL — MÓDULO 03",
         font=f_sub, fg=MUTED, bg=BG).pack()
tk.Label(frame_header, text="QUIZ DE QUÍMICA",
         font=f_title, fg=GREEN, bg=BG).pack()
tk.Label(frame_header, text="Reações Químicas  ·  Lei de Lavoisier  ·  10.º Ano",
         font=f_sub, fg=MUTED, bg=BG).pack(pady=(2,0))

# ── Score bar ─────────────────────────────────────────────────────
frame_score = tk.Frame(janela, bg=PANEL, highlightbackground=BORDER,
                        highlightthickness=1)
frame_score.pack(fill="x", padx=30, pady=6)

def make_stat(parent, label, color):
    f = tk.Frame(parent, bg=PANEL)
    f.pack(side="left", expand=True, pady=6)
    val = tk.Label(f, text="0", font=f_score_v, fg=color, bg=PANEL)
    val.pack()
    tk.Label(f, text=label, font=tkfont.Font(family="Courier New", size=8),
             fg=MUTED, bg=PANEL).pack()
    return val

lbl_correct = make_stat(frame_score, "CERTAS",   GREEN)
lbl_wrong   = make_stat(frame_score, "ERRADAS",  RED)
lbl_qnum    = make_stat(frame_score, "QUESTÃO",  YELLOW)
lbl_streak  = make_stat(frame_score, "SEQUÊNCIA 🔥", BLUE)

# ── Barra de progresso ────────────────────────────────────────────
frame_prog = tk.Frame(janela, bg="#111111", height=5)
frame_prog.pack(fill="x", padx=30)
frame_prog.pack_propagate(False)
canvas_prog = tk.Canvas(frame_prog, bg="#111111", height=5,
                         highlightthickness=0, bd=0)
canvas_prog.pack(fill="both")
prog_rect = canvas_prog.create_rectangle(0, 0, 0, 5, fill=GREEN, outline="")

def update_progress(fraction):
    janela.update_idletasks()
    w = canvas_prog.winfo_width()
    canvas_prog.coords(prog_rect, 0, 0, int(w * fraction), 5)

# ── Área principal (quiz + resultado) ────────────────────────────
frame_main = tk.Frame(janela, bg=BG)
frame_main.pack(fill="both", expand=True, padx=30, pady=4)

# ════════════════════════
# TELA QUIZ
# ════════════════════════
frame_quiz = tk.Frame(frame_main, bg=BG)
frame_quiz.pack(fill="both", expand=True)

# Card da pergunta
frame_card = tk.Frame(frame_quiz, bg=PANEL,
                       highlightbackground=BORDER, highlightthickness=1)
frame_card.pack(fill="x", pady=(0,8))

# Barra decorativa topo
tk.Frame(frame_card, bg=GREEN, height=3).pack(fill="x")

frame_meta = tk.Frame(frame_card, bg=PANEL)
frame_meta.pack(fill="x", padx=20, pady=(10,0))
lbl_qnum_card = tk.Label(frame_meta, text="QUESTÃO 1 / 15",
                          font=f_meta, fg=MUTED, bg=PANEL)
lbl_qnum_card.pack(side="left")
lbl_diff = tk.Label(frame_meta, text="FÁCIL",
                     font=f_meta, fg=GREEN, bg=PANEL)
lbl_diff.pack(side="right")

lbl_question = tk.Label(frame_card, text="", font=f_q, fg=WHITE,
                          bg=PANEL, wraplength=740, justify="left")
lbl_question.pack(padx=20, pady=8, anchor="w")

# Opções
frame_opts = tk.Frame(frame_quiz, bg=BG)
frame_opts.pack(fill="x", pady=2)

# Feedback
frame_fb = tk.Frame(frame_quiz, bg=BG)
frame_fb.pack(fill="x", pady=4)
lbl_fb = tk.Label(frame_fb, text="", font=f_exp, fg=TEXT,
                   bg=PANEL, wraplength=740, justify="left",
                   padx=16, pady=12)

# Botão próxima
btn_next = tk.Button(frame_quiz, text="PRÓXIMA  →", font=f_btn,
                      bg=BG, fg=GREEN, activebackground=GREEN,
                      activeforeground=BG, relief="flat",
                      highlightbackground=GREEN, highlightthickness=2,
                      padx=20, pady=8, cursor="hand2",
                      command=lambda: next_question())
# ════════════════════════
# TELA RESULTADO
# ════════════════════════
frame_result = tk.Frame(frame_main, bg=BG)

lbl_res_title = tk.Label(frame_result, text="ANÁLISE CONCLUÍDA",
                           font=f_result, fg=GREEN, bg=BG)
lbl_res_title.pack(pady=(20,4))

# Círculo de resultado (simulado com canvas)
canvas_circle = tk.Canvas(frame_result, width=180, height=180,
                            bg=BG, highlightthickness=0)
canvas_circle.pack(pady=10)
canvas_circle.create_oval(10,10,170,170, outline=GREEN, width=3)
lbl_pct = canvas_circle.create_text(90, 82, text="0%",
                                      font=f_pct, fill=GREEN)
canvas_circle.create_text(90, 140, text="ACERTOS",
                           font=tkfont.Font(family="Courier New", size=9),
                           fill=MUTED)

lbl_grade = tk.Label(frame_result, text="", font=f_result, bg=BG)
lbl_grade.pack(pady=6)

frame_rb = tk.Frame(frame_result, bg=BG)
frame_rb.pack(pady=10)

def rb_stat(parent, color, label):
    f = tk.Frame(parent, bg=BG)
    f.pack(side="left", padx=26)
    v = tk.Label(f, text="0", font=f_score_v, fg=color, bg=BG)
    v.pack()
    tk.Label(f, text=label, font=tkfont.Font(family="Courier New", size=8),
             fg=MUTED, bg=BG).pack()
    return v

rb_c = rb_stat(frame_rb, GREEN,  "CERTAS")
rb_w = rb_stat(frame_rb, RED,    "ERRADAS")
rb_s = rb_stat(frame_rb, BLUE,   "MAX STREAK")

btn_restart = tk.Button(frame_result, text="↺  RECOMEÇAR", font=f_btn,
                         bg=BG, fg=YELLOW, activebackground=YELLOW,
                         activeforeground=BG, relief="flat",
                         highlightbackground=YELLOW, highlightthickness=2,
                         padx=24, pady=12, cursor="hand2",
                         command=lambda: restart())
btn_restart.pack(pady=20)

# ══════════════════════════════════════════════════════════════════
# LÓGICA
# ══════════════════════════════════════════════════════════════════

def update_score_bar():
    lbl_correct.config(text=str(correct))
    lbl_wrong.config(text=str(wrong))
    lbl_qnum.config(text=f"{min(qi+1, len(questions))}/{len(questions)}")
    lbl_streak.config(text=str(streak))
    update_progress(qi / len(questions))

def load_question():
    global answered, option_buttons
    answered = False

    q = questions[qi]
    n = qi + 1

    lbl_qnum_card.config(text=f"QUESTÃO {n} / {len(questions)}")

    diff_color = RED if q["diff"] == "DIFÍCIL" else (YELLOW if q["diff"] == "MÉDIO" else GREEN2)
    lbl_diff.config(text=q["diff"], fg=diff_color)
    lbl_question.config(text=q["text"])

    # Limpa opções anteriores
    for w in frame_opts.winfo_children():
        w.destroy()
    option_buttons = []

    letters = ["A", "B", "C", "D"]
    for i, opt in enumerate(q["opts"]):
        btn = tk.Button(
            frame_opts,
            text=f"  {letters[i]}   {opt}",
            font=f_opt,
            fg=TEXT, bg="#0b1a12",
            activebackground=BORDER,
            activeforeground=GREEN,
            relief="flat",
            anchor="w",
            padx=14, pady=7,
            highlightbackground=BORDER,
            highlightthickness=1,
            cursor="hand2",
            wraplength=720,
            justify="left"
        )
        idx = i
        btn.config(command=lambda i=idx: choose(i))
        btn.pack(fill="x", pady=2)
        # Hover
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#0d2a1f", fg=GREEN,
                                                        highlightbackground=GREEN))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#0b1a12", fg=TEXT,
                                                        highlightbackground=BORDER)
                  if b.cget("bg") not in (RED, "#042010", "#1a0008") else None)
        option_buttons.append(btn)

    # Esconde feedback e botão próxima
    lbl_fb.pack_forget()
    btn_next.pack_forget()
    update_score_bar()

def choose(idx):
    global answered, correct, wrong, streak, max_streak
    if answered:
        return
    answered = True

    q = questions[qi]
    for b in option_buttons:
        b.config(state="disabled", cursor="arrow")
        b.unbind("<Enter>")
        b.unbind("<Leave>")

    if idx == q["ans"]:
        option_buttons[idx].config(bg="#042010", fg=GREEN,
                                    highlightbackground=GREEN)
        correct += 1
        streak  += 1
        if streak > max_streak:
            max_streak = streak
        streak_txt = f"  ✓ CORRETO{f'  — {streak}× SEQUÊNCIA 🔥' if streak>1 else ''}\n\n" + q["exp"]
        lbl_fb.config(text=streak_txt, bg="#042010", fg="#a0ffcc",
                       highlightbackground=GREEN, highlightthickness=1)
    else:
        option_buttons[idx].config(bg="#1a0008", fg=RED,
                                    highlightbackground=RED)
        option_buttons[q["ans"]].config(bg="#042010", fg=GREEN,
                                         highlightbackground=GREEN)
        wrong  += 1
        streak  = 0
        lbl_fb.config(text="  ✗ INCORRETO\n\n" + q["exp"],
                       bg="#1a0008", fg="#ffaabb",
                       highlightbackground=RED, highlightthickness=1)

    lbl_fb.pack(fill="x", pady=4)
    btn_next.pack(fill="x", pady=6)
    update_score_bar()

def next_question():
    global qi
    qi += 1
    if qi >= len(questions):
        show_result()
    else:
        load_question()

def show_result():
    frame_quiz.pack_forget()
    frame_result.pack(fill="both", expand=True)
    update_progress(1.0)

    pct = round(correct / len(questions) * 100)
    canvas_circle.itemconfig(lbl_pct, text=f"{pct}%")

    if pct >= 90:
        grade, color = "⚗  QUÍMICO MESTRE", GREEN
    elif pct >= 70:
        grade, color = "🔬  BOM TRABALHO!", YELLOW
    elif pct >= 50:
        grade, color = "📚  CONTINUA A ESTUDAR", BLUE
    else:
        grade, color = "💀  REVISÃO URGENTE", RED

    canvas_circle.itemconfig(lbl_pct, fill=color)
    lbl_grade.config(text=grade, fg=color)
    rb_c.config(text=str(correct))
    rb_w.config(text=str(wrong))
    rb_s.config(text=str(max_streak))

def restart():
    global questions, qi, correct, wrong, streak, max_streak, answered
    questions  = random.sample(QUESTIONS, len(QUESTIONS))
    qi = correct = wrong = streak = max_streak = 0
    answered = False
    frame_result.pack_forget()
    frame_quiz.pack(fill="both", expand=True)
    load_question()

# ── Inicia ────────────────────────────────────────────────────────
restart()
janela.mainloop()