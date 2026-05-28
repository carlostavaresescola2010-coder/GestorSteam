# ================================
#        FUNÇÕES DO CÓDIGO PRINCIPAL
# ================================

# --------------------------
# LISTA e TUPLOS
# --------------------------
# Aqui a lista contém TUPLOS (nome, email, atividade)
def contar_por_atividade(atividade, participantes):
    """
    Conta quantos participantes estão inscritos
    numa determinada atividade.
    """

    # percorre cada tuplo 'p' na LISTA 'participantes' e soma 1 se p[2] == atividade
    # p[2]=terceiro elemento do tuplo: a atividade do participante
    return sum(1 for p in participantes if p[2] == atividade)



#git funcionando!!


# --------------------------
# LIMPAR CAMPOS DO FORMULÁRIO
# --------------------------
def limpar_campos(ent_nome, ent_email, tk, combo):
    """
    Limpa os campos do formulário após registo.
    """
    # DELETE do Entry: remove todo o texto do campo
    ent_nome.delete(0, tk.END)
    ent_email.delete(0, tk.END)
    # SET do Combobox: retorna para valor padrão
    combo.set("Selecione...")

#o stor é o maior



#funcionando prof!
# --------------------------
# LISTA, TUPLOS, FILTRO
# --------------------------
def atualizar_visualizacao(participantes, listbox, ent_filtro, atividades_base, lbl_contador, tk):
    """
    Atualiza a listbox da aba de consulta.
    Mostra participantes organizados por atividade.
    Também aplica filtro por email ou atividade.
    """

    # Limpa listbox antes de atualizar
    listbox.delete(0, tk.END)

    # Pega o termo digitado no campo de filtro e converte para minúsculo
    termo = ent_filtro.get().lower()

    # Contador do número total de participantes mostrados
    contador_total = 0

    # Percorre cada atividade da lista 'atividades_base' em ordem alfabética
    for atividade in sorted(atividades_base):

        # Cria uma LISTA temporária de participantes desta atividade
        # Cada item da lista é um TUPLO (nome, email, atividade) #lista e tuplos
        participantes_atividade = [
            p for p in participantes if p[2] == atividade
        ]

        # Se não houver, pula para a próxima
        if not participantes_atividade:
            continue

        # Mostra título da atividade na listbox (com contador de inscritos)
        listbox.insert(
            tk.END,
            f"=== {atividade} ({len(participantes_atividade)}/5) ==="
        )

        # --------------------------
        # DESCONSTRUÇÃO DE TUPLOS
        # --------------------------
        # Para cada participante da atividade, pegamos nome e email
        # O "_" significa que ignoramos o terceiro elemento (atividade), pois já sabemos qual é
        for nome, email, _ in participantes_atividade:

            # Aplica filtro: se o termo estiver no email ou na atividade
            if termo in email.lower() or termo in atividade.lower(): #converte
                # Insere participante na listbox com indentação
                listbox.insert(tk.END, f"  {nome} | {email}")
                contador_total += 1

        # Insere linha em branco entre atividades
        listbox.insert(tk.END, "")

    # Atualiza o label com o número total de inscritos exibidos
    lbl_contador.config(text=f"Total de inscritos: {contador_total}")

if __name__ == "main":
    contar_por_atividade()