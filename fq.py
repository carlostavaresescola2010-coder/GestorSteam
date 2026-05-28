import tkinter as tk
import random
import math

# Configurações
largura = 720
altura = 420
num_moleculas = 50
moleculas = []

# Janela principal
janela = tk.Tk()
janela.title("⚗️ Simulação Molecular")
janela.geometry("820x750")
janela.configure(bg="#0d0d1a")
janela.resizable(False, False)

temperatura = tk.IntVar(value=20)

# ── Paleta de cores ──────────────────────────────────────────────
COR_FUNDO      = "#0d0d1a"
COR_CANVAS     = "#0a0a18"
COR_SOLIDO     = "#00e5ff"   # ciano
COR_LIQUIDO    = "#4fc3f7"   # azul claro
COR_GASOSO     = "#ff5252"   # vermelho
COR_TEXTO      = "#e0e0ff"
COR_ACENTO     = "#7c4dff"

def get_cor_molecula(temp):
    if temp < 0:
        return "#00e5ff"      # gelo — ciano brilhante
    elif temp < 30:
        return "#26c6da"      # sólido — azul teal
    elif temp < 70:
        return "#4fc3f7"      # líquido — azul claro
    elif temp < 150:
        return "#ffb300"      # gás — laranja
    else:
        return "#ff5252"      # plasma — vermelho intenso

def get_velocidade(temp):
    """Velocidade cresce de forma muito mais visível com a temperatura."""
    if temp <= 0:
        return max(0.1, (temp + 1000) / 3000)   # quase parado no frio extremo
    elif temp < 30:
        return 0.5
    elif temp < 70:
        return 2.0
    elif temp < 150:
        # escala suave entre 2 e 8
        return 2.0 + (temp - 70) / 80 * 6
    else:
        # acima de 150: escala agressiva
        return 8.0 + (temp - 150) / 50 * 6

def estado_da_materia(temp):
    if temp < 30:
        return "SÓLIDO", COR_SOLIDO
    elif temp < 70:
        return "LÍQUIDO", COR_LIQUIDO
    else:
        return "GASOSO", COR_GASOSO

# ── Título ────────────────────────────────────────────────────────
frame_titulo = tk.Frame(janela, bg=COR_FUNDO)
frame_titulo.pack(fill="x", pady=(18, 4))

tk.Label(
    frame_titulo,
    text="⚗  SIMULAÇÃO MOLECULAR",
    font=("Courier New", 20, "bold"),
    fg=COR_ACENTO,
    bg=COR_FUNDO
).pack()

tk.Label(
    frame_titulo,
    text="Movimento das partículas segundo a temperatura",
    font=("Courier New", 10),
    fg="#888899",
    bg=COR_FUNDO
).pack()

# ── Canvas ────────────────────────────────────────────────────────
canvas_frame = tk.Frame(janela, bg="#1a1a2e", bd=2, relief="flat")
canvas_frame.pack(padx=30, pady=6)

canvas = tk.Canvas(
    canvas_frame,
    width=largura,
    height=altura,
    bg=COR_CANVAS,
    highlightthickness=0
)
canvas.pack()

# Borda brilhante com linha decorativa
canvas.create_rectangle(2, 2, largura-2, altura-2,
                         outline=COR_ACENTO, width=1, dash=(6,4))

# ── Painel de info ────────────────────────────────────────────────
frame_info = tk.Frame(janela, bg=COR_FUNDO)
frame_info.pack(pady=4)

label_temp = tk.Label(
    frame_info,
    text="🌡  Temperatura: 20 °C",
    font=("Courier New", 13, "bold"),
    fg=COR_TEXTO,
    bg=COR_FUNDO
)
label_temp.pack(side="left", padx=30)

label_estado = tk.Label(
    frame_info,
    text="◈  Estado: SÓLIDO",
    font=("Courier New", 13, "bold"),
    fg=COR_SOLIDO,
    bg=COR_FUNDO
)
label_estado.pack(side="left", padx=30)

label_vel = tk.Label(
    frame_info,
    text="⚡ Velocidade: 0.5×",
    font=("Courier New", 11),
    fg="#888899",
    bg=COR_FUNDO
)
label_vel.pack(side="left", padx=20)

# ── Slider ────────────────────────────────────────────────────────
frame_slider = tk.Frame(janela, bg=COR_FUNDO)
frame_slider.pack(pady=6)

tk.Label(frame_slider, text="TEMPERATURA  (°C)", font=("Courier New", 10),
         fg="#888899", bg=COR_FUNDO).pack()

slider = tk.Scale(
    frame_slider,
    variable=temperatura,
    from_=-200,
    to=500,
    orient="horizontal",
    length=560,
    bg=COR_FUNDO,
    fg=COR_TEXTO,
    troughcolor="#1a1a2e",
    activebackground=COR_ACENTO,
    highlightthickness=0,
    sliderlength=28,
    font=("Courier New", 9),
    showvalue=False,
    relief="flat",
    bd=0
)
slider.pack()

# Rótulos dos extremos
frame_extremos = tk.Frame(frame_slider, bg=COR_FUNDO)
frame_extremos.pack(fill="x")
tk.Label(frame_extremos, text="-200°C  🧊", font=("Courier New", 9),
         fg=COR_SOLIDO, bg=COR_FUNDO).pack(side="left")
tk.Label(frame_extremos, text="🔥  500°C", font=("Courier New", 9),
         fg=COR_GASOSO, bg=COR_FUNDO).pack(side="right")

# ── Botões de estado ──────────────────────────────────────────────
frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
frame_botoes.pack(pady=16)

tk.Label(frame_botoes, text="PRESET RÁPIDO:", font=("Courier New", 10),
         fg="#888899", bg=COR_FUNDO).pack(side="left", padx=(0,12))

def estilo_botao(master, texto, cor_bg, cor_fg, cmd):
    return tk.Button(
        master,
        text=texto,
        command=cmd,
        font=("Courier New", 14, "bold"),
        bg=cor_bg,
        fg=cor_fg,
        activebackground=cor_fg,
        activeforeground=cor_bg,
        relief="flat",
        bd=0,
        padx=28,
        pady=14,
        cursor="hand2"
    )

def definir_estado(estado):
    if estado == "Sólido":
        temperatura.set(10)
    elif estado == "Líquido":
        temperatura.set(50)
    else:
        temperatura.set(250)

btn_s = estilo_botao(frame_botoes, "🧊  SÓLIDO",  "#003d4d", COR_SOLIDO,  lambda: definir_estado("Sólido"))
btn_l = estilo_botao(frame_botoes, "💧  LÍQUIDO", "#003060", COR_LIQUIDO, lambda: definir_estado("Líquido"))
btn_g = estilo_botao(frame_botoes, "🔥  GASOSO",  "#3d0000", COR_GASOSO,  lambda: definir_estado("Gasoso"))

btn_s.pack(side="left", padx=8)
btn_l.pack(side="left", padx=8)
btn_g.pack(side="left", padx=8)

# Hover effect simples
def on_enter(btn, cor_fg, cor_bg):
    btn.config(bg=cor_fg, fg=cor_bg)

def on_leave(btn, cor_bg, cor_fg):
    btn.config(bg=cor_bg, fg=cor_fg)

btn_s.bind("<Enter>", lambda e: on_enter(btn_s, COR_SOLIDO,  "#003d4d"))
btn_s.bind("<Leave>", lambda e: on_leave(btn_s, "#003d4d", COR_SOLIDO))
btn_l.bind("<Enter>", lambda e: on_enter(btn_l, COR_LIQUIDO, "#003060"))
btn_l.bind("<Leave>", lambda e: on_leave(btn_l, "#003060", COR_LIQUIDO))
btn_g.bind("<Enter>", lambda e: on_enter(btn_g, COR_GASOSO,  "#3d0000"))
btn_g.bind("<Leave>", lambda e: on_leave(btn_g, "#3d0000", COR_GASOSO))

# ── Criação das moléculas ─────────────────────────────────────────
def criar_moleculas():
    moleculas.clear()
    canvas.delete("mol")
    for _ in range(num_moleculas):
        x = random.randint(20, largura - 20)
        y = random.randint(20, altura - 20)
        # direção aleatória normalizada
        angulo = random.uniform(0, 2 * math.pi)
        dx = math.cos(angulo)
        dy = math.sin(angulo)
        bola = canvas.create_oval(x, y, x+10, y+10,
                                   fill=COR_SOLIDO, outline="", tags="mol")
        moleculas.append([bola, dx, dy])

# ── Loop de animação ──────────────────────────────────────────────
def mover():
    temp  = temperatura.get()
    vel   = get_velocidade(temp)
    cor   = get_cor_molecula(temp)
    estado, cor_estado = estado_da_materia(temp)

    for m in moleculas:
        bola, dx, dy = m

        # Adicionar pequena perturbação aleatória para parecer mais natural
        if vel > 1:
            m[1] += random.uniform(-0.15, 0.15)
            m[2] += random.uniform(-0.15, 0.15)
            # Renormalizar para não acumular velocidade infinita
            mag = math.hypot(m[1], m[2])
            if mag > 0:
                m[1] /= mag
                m[2] /= mag

        canvas.move(bola, m[1] * vel, m[2] * vel)
        x1, y1, x2, y2 = canvas.coords(bola)

        if x1 <= 0 or x2 >= largura:
            m[1] = -m[1]
        if y1 <= 0 or y2 >= altura:
            m[2] = -m[2]

        canvas.itemconfig(bola, fill=cor)

    label_temp.config(text=f"🌡  Temperatura: {temp} °C")
    label_estado.config(text=f"◈  Estado: {estado}", fg=cor_estado)
    label_vel.config(text=f"⚡ Velocidade: {vel:.1f}×")

    janela.after(20, mover)

# ── Inicializa ────────────────────────────────────────────────────
criar_moleculas()
mover()
janela.mainloop()