#ler os nomes do ficheiro original
nome = []
with open("nome.txt", "r") as f:
    for linha in f:
        nomes.append(linha.strip())

#ordenar
nomes. sort

#gravar novo ficheiro
with open("nome.ordenados", "w") as f:
    for nome in nomes:
        f.write(nome)