# ==================================
# Sistema de Gestão de Turma (SEM CLASS)
# ==================================

# ---------- DADOS ----------
turma = []


# ---------- FUNÇÕES DE VALIDAÇÃO ----------
def ler_nome(mensagem="Nome"):
    while True:
        nome = input(f"{mensagem}: ").strip()
        if nome and nome.replace(" ", "").isalpha():
            return nome
        print("❌ Valor inválido. Use apenas letras.")


def ler_idade():
    while True:
        idade = input("Idade (>=15): ")
        if idade.isdigit() and 15 <= int(idade) <= 90:
            return int(idade)
        print("❌ Idade inválida.")


def ler_nota():
    while True:
        try:
            nota = float(input("Nota (0 a 20): "))
            if 0 <= nota <= 20:
                return nota
        except ValueError:
            pass
        print("❌ Nota inválida.")


def escolher_indice(maximo):
    while True:
        escolha = input("Número do aluno: ")
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < maximo:
                return indice
        print("❌ Aluno inválido.")


# ---------- FUNÇÕES PRINCIPAIS ----------
def adicionar_aluno():
    aluno = {
        "nome": ler_nome("Nome do aluno"),
        "idade": ler_idade(),
        "nota": ler_nota(),
        "curso": ler_nome("Curso"),
        "faltas_presenca": 0,
        "faltas_disciplina": 0,
        "faltas_material": 0
    }

    turma.append(aluno)
    print("✅ Aluno adicionado com sucesso!")


def listar_alunos():
    if not turma:
        print("⚠️ Não existem alunos registados.")
        return False

    print("\n📋 Lista de Alunos")
    for i, aluno in enumerate(turma, start=1):  #indice e valor
        print(
            f"\n{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | "
            f"Nota: {aluno['nota']} | Curso: {aluno['curso']}"
        )
        print(
            f"   Faltas -> Presença: {aluno['faltas_presenca']}, "
            f"Disciplina: {aluno['faltas_disciplina']}, "
            f"Material: {aluno['faltas_material']}"
        )
    return True


def remove96r_aluno():
    if not listar_alunos():
        return

    indice = escolher_indice(len(turma))
    aluno = turma[indice]

    confirmacao = input(
        f"Tem certeza que deseja remover '{aluno['nome']}'? (S/N): "
    ).strip().upper()

    if confirmacao == "S":
        turma.pop(indice)
        print("🗑️ Aluno removido com sucesso!")
    else:
        print("❎ Remoção cancelada.")


def menu_faltas():
    print("\nTipo de falta:")
    print("1 - Falta de presença")
    print("2 - Falta disciplinar")
    print("3 - Falta de material")
    return input("Escolha: ")


def marcar_falta():
    if not listar_alunos():
        return

    indice = escolher_indice(len(turma))
    tipo = menu_faltas()

    while tipo not in ("1", "2", "3"):
        print("❌ Tipo inválido.")
        tipo = menu_faltas()

    aluno = turma[indice]

    if tipo == "1":
        aluno["faltas_presenca"] += 1
    elif tipo == "2":
        aluno["faltas_disciplina"] += 1
    elif tipo == "3":
        aluno["faltas_material"] += 1

    print("⚠️ Falta registada com sucesso!")


def estatisticas_aluno():
    if not listar_alunos():
        return

    indice = escolher_indice(len(turma))
    aluno = turma[indice] #busca

    total_faltas = (
        aluno["faltas_presenca"]
        + aluno["faltas_disciplina"]
        + aluno["faltas_material"]
    )

    print("\n📊 Estatísticas do Aluno")
    print(f"Nome: {aluno['nome']}")
    print(f"Curso: {aluno['curso']}")
    print(f"Nota: {aluno['nota']}")
    print(f"Total de faltas: {total_faltas}")
    print(f"- Presença: {aluno['faltas_presenca']}")
    print(f"- Disciplina: {aluno['faltas_disciplina']}")
    print(f"- Material: {aluno['faltas_material']}")


def listar_por_curso():
    if not turma:
        print("⚠️ Não existem alunos.")
        return

    cursos = {}

    for aluno in turma:
        cursos.setdefault(aluno["curso"], []).append(aluno)

    print("\n📚 Alunos por Curso")
    for curso, alunos in cursos.items():
        print(f"\n🎓 Curso: {curso}")
        for aluno in alunos:
            print(f"- {aluno['nome']}")


def estatisticas_turma_por_curso():
    if not turma:
        print("⚠️ Não existem alunos.")
        return

    cursos = list({aluno["curso"] for aluno in turma})

    print("\nCursos disponíveis:")
    for i, curso in enumerate(cursos, start=1):
        print(f"{i} - {curso}")

    while True:
        escolha = input("Escolha o curso pelo número: ")
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(cursos):
                curso_escolhido = cursos[indice]
                break
        print("❌ Curso inválido.")

    alunos_curso = [a for a in turma if a["curso"] == curso_escolhido] #nova lista

    presenca = sum(a["faltas_presenca"] for a in alunos_curso)
    disciplina = sum(a["faltas_disciplina"] for a in alunos_curso)
    material = sum(a["faltas_material"] for a in alunos_curso)

    print(f"\n📈 Estatísticas do Curso: {curso_escolhido}")
    print(f"Número de alunos: {len(alunos_curso)}")
    print(f"Faltas de presença: {presenca}")
    print(f"Faltas disciplinares: {disciplina}")
    print(f"Faltas de material: {material}")


# ---------- MENU ----------
def menu():
    print("\n====== GESTOR DE TURMA ======")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Marcar falta")
    print("4 - Estatísticas de um aluno")
    print("5 - Estatísticas da turma por curso")
    print("6 - Remover aluno")
    print("7 - Listar alunos por curso")
    print("0 - Sair")
    return input("Escolha uma opção: ")


# ---------- PROGRAMA PRINCIPAL ----------
def main():
    while True:
        opcao = menu()

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            marcar_falta()
        elif opcao == "4":
            estatisticas_aluno()
        elif opcao == "5":
            estatisticas_turma_por_curso()
        elif opcao == "6":
            remover_aluno()
        elif opcao == "7":
            listar_por_curso()
        elif opcao == "0":
            print("👋 Programa encerrado.")
            break
        else:
            print("❌ Opção inválida.")

main()

