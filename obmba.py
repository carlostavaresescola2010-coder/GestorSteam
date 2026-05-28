import tkinter as tk
from tkinter import messagebox
import math

def simular():
    try:
        A0 = float(entry_A0.get())
        k = float(entry_k.get())

        canvas.delete("all")  # Limpa o gráfico anterior

        largura = 500
        altura = 300
        margem = 40

        # Desenhar eixos
        canvas.create_line(margem, altura - margem, largura - margem, altura - margem)  # eixo X
        canvas.create_line(margem, margem, margem, altura - margem)  # eixo Y

        tempo_max = 20
        pontos = []

        # Calcular pontos da reação
        for t in range(0, tempo_max + 1):
            concentracao = A0 * math.exp(-k * t)

            # Converter para coordenadas do canvas
            x = margem + (t / tempo_max) * (largura - 2 * margem)
            y = (altura - margem) - (concentracao / A0) * (altura - 2 * margem)

            pontos.append((x, y))

        # Desenhar curva
        for i in range(len(pontos) - 1):
            canvas.create_line(pontos[i][0], pontos[i][1],
                               pontos[i+1][0], pontos[i+1][1],
                               width=2)

    except ValueError:
        messagebox.showerror("Erro", "Introduza valores numéricos válidos!")

# Criar janela
janela = tk.Tk()
janela.title("Simulação Reação de 1ª Ordem")
janela.geometry("600x450")

tk.Label(janela, text="Concentração Inicial (A0):").pack()
entry_A0 = tk.Entry(janela)
entry_A0.pack()

tk.Label(janela, text="Constante de Velocidade (k):").pack()
entry_k = tk.Entry(janela)
entry_k.pack()

tk.Button(janela, text="Simular", command=simular).pack(pady=10)

canvas = tk.Canvas(janela, width=500, height=300, bg="white")
canvas.pack()

janela.mainloop()