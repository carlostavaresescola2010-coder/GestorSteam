# Notas De Escola
while True:
    try:
        quantidade = int(input("Quantas notas quer inserir? "))
        if quantidade > 0:
            break
        print("❌ Digite um número maior que zero.")
    except ValueError:
        print("❌ Não é válido. Digite um número inteiro!")

notas = []
contador = 0

while contador < quantidade:
    try:
        nota = float(input(f"Insira a nota {contador + 1}: "))

        # Verifica se a nota é entre (0 a 20)
        if 0 <= nota <= 20:
            notas.append(nota)
            contador += 1
        else:
            print("⚠️ Nota inválida! Insira um valor entre 0 e 20.")

    except ValueError:
        print("❌ Erro: Isso não é um número. Tente novamente.")

#RESULTADOS
print("\n" + "=" * 20)
print(f"Notas: {notas}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")

media = sum(notas) / len(notas)
print(f"Média:  {media:.2f}")

# APROVAÇÃO
if media >= 10:
    print("Estado: ✅ APROVADO")
else:
    print("Estado: ❌ REPROVADO")
print("=" * 20)


