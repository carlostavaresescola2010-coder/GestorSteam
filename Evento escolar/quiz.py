import random
from tkinter import messagebox
from tkinter.simpledialog import askstring


def iniciar_quiz():

    perguntas = [
        {
            "pergunta": "Quantos jogadores tem uma equipa de Futebol?",
            "resposta": "11"
        },
        {
            "pergunta": "Que atividade usa um tabuleiro e peças?",
            "resposta": "Xadrez"
        },
        {
            "pergunta": "Qual destas é um desporto aquático?",
            "resposta": "Kitesurf"
        },
        {
            "pergunta": "Em que atividade se usa uma bola laranja grande?",
            "resposta": "Basquetebol"
        },
        {
            "pergunta": "Que atividade envolve escalar paredes?",
            "resposta": "Escalada Radical"
        }
    ]

    pontuacao = 0

    # Escolhe 3 perguntas aleatórias
    perguntas_sorteadas = random.sample(perguntas, 3)

    for i, p in enumerate(perguntas_sorteadas, 1):

        resposta = askstring(
            f"Quiz - Pergunta {i}",
            p["pergunta"]
        )

        if resposta and resposta.lower() == p["resposta"].lower():
            pontuacao += 1
            messagebox.showinfo("Resultado", "✅ Correto!")
        else:
            messagebox.showerror(
                "Resultado",
                f"❌ Errado! A resposta correta é: {p['resposta']}"
            )

    messagebox.showinfo(
        "Pontuação Final",
        f"Terminaste o quiz!\nPontuação: {pontuacao} / 3"
    )