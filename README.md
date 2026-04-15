# Projeto Gestor de Steam - CRUD Utilizador e Jogo

## 📘 Descrição do Projeto

Este projeto foi desenvolvido com fins pedagógicos para alunos do **Curso Profissional de Gestão e Programação de Sistemas Informáticos (GPSI) – 10.º ano**.

O objetivo principal é demonstrar como implementar operações **CRUD (Create, Read, Update, Delete)** em Python utilizando:

* funções (sem classes)
* dicionários
* separação por ficheiros
* validação de dados
* menus em terminal
* códigos de retorno ao estilo HTTP

O projeto simula a gestão das entidades **Utilizador** e **Jogo** num sistema inspirado na plataforma Steam.

---

## 🎯 Objetivos Pedagógicos

Com este projeto os alunos devem aprender a:

* organizar código em múltiplos ficheiros Python
* utilizar dicionários como estrutura de armazenamento
* implementar operações CRUD
* validar dados introduzidos pelo utilizador
* gerar identificadores automáticos
* trabalhar com datas em Python
* separar lógica de negócio da interface (menu)
* utilizar códigos de retorno para comunicar o resultado das operações
* tratar erros com `try/except`

---

## 📂 Estrutura do Projeto

```
.
└── gestor_steam/
     ├── main.py
     ├── utilizadores.py
     ├── jogos.py
     ├── utils.py
     └── README.md
```

### main.py

Contém o **menu interativo em terminal**.
Responsável apenas por:

* apresentar opções ao utilizador
* recolher dados introduzidos — **todos os `input()` ficam aqui**
* chamar funções dos módulos `utilizadores` e `jogos`
* verificar os códigos de retorno e mostrar mensagens ao utilizador
* repetir o pedido de dados em caso de erro (`400` ou `404`)

Não contém validações — essas ficam nos respetivos módulos.

---

### utilizadores.py

Contém todas as operações CRUD da entidade **Utilizador**.
Não tem nenhum `input()` — só recebe dados, valida e retorna um código.

Funções disponíveis:

* `criar_utilizador(nome, username, email, password, nascimento)`
* `listar_utilizadores()`
* `consultar_utilizador(uid)`
* `atualizar_utilizador(uid, nome, username, email, password, nascimento)`
* `remover_utilizador(uid)`

Os utilizadores são guardados num **dicionário em memória**.

---

### jogos.py

Contém todas as operações CRUD da entidade **Jogo**.
Não tem nenhum `input()` — só recebe dados, valida e retorna um código.

Funções disponíveis:

* `criar_jogo(nome, modo, idade_minima, tamanho_gb)`
* `listar_jogos()`
* `consultar_jogo(jid)`
* `atualizar_jogo(jid, nome, modo, idade_minima, tamanho_gb)`
* `remover_jogo(jid)`

Os jogos são guardados num **dicionário em memória**.

---

### utils.py

Contém funções auxiliares partilhadas por `utilizadores.py` e `jogos.py`.
Não é importado pelo `main.py`.

* `gerar_id_utilizador()` — gera IDs no formato `U001`, `U002`, ...
* `gerar_id_jogo()` — gera IDs no formato `J001`, `J002`, ...
* `validar_data(data)` — valida formato `DD/MM/AAAA` e ano entre 1900 e o ano atual
* `validar_email(email)` — valida se o email contém `@` e `.`

---

## 👤 Estrutura da Entidade Utilizador

Cada utilizador contém:

* `id` — gerado automaticamente (ex: `U001`)
* `nome` — nome verdadeiro da pessoa
* `username` — nome de utilizador na plataforma
* `email` — obrigatório, com formato válido
* `password`
* `nascimento` — data no formato `DD/MM/AAAA`

Exemplo:

```
U001
Nome:       Ana Silva
Username:   anasilva99
Email:      ana@email.pt
Password:   ********
Nascimento: 12/03/2007
```

---

## 🎮 Estrutura da Entidade Jogo

Cada jogo contém:

* `id` — gerado automaticamente (ex: `J001`)
* `nome` — nome do jogo
* `modo` — `single player`, `multiplayer` ou `ambos`
* `idade_minima` — número inteiro
* `tamanho_gb` — número em GB

Exemplo:

```
J001
Nome:        Uncharted 4
Modo:        single player
Idade min.:  16+
Tamanho:     50.0 GB
```

---

## 🔁 Códigos de Retorno

Todas as funções de `utilizadores.py` e `jogos.py` retornam um tuplo com:

* `return_code[0]` — código numérico do resultado
* `return_code[1]` — mensagem ou valor (ex: ID gerado)

| Código | Significado | Exemplo |
|---|---|---|
| `201` | Criado com sucesso | `(201, "U001")` |
| `200` | Operação com sucesso | `(200, "Utilizador atualizado com sucesso.")` |
| `400` | Dados inválidos | `(400, "Email invalido.")` |
| `404` | Registo não encontrado | `(404, "Utilizador nao encontrado.")` |
| `500` | Erro interno inesperado | `(500, "mensagem de erro")` |

No `main.py` o resultado é verificado e mostrado assim:

```python
return_code = criar_utilizador(nome, username, email, password, nascimento)
if return_code[0] == 201:
    print(f"  [{return_code[0]}] Utilizador criado com sucesso. ID: {return_code[1]}")
elif return_code[0] == 400:
    print(f"  [{return_code[0]}] {return_code[1]}")
elif return_code[0] == 500:
    print(f"  [{return_code[0]}] Internal Error: {return_code[1]}")
```

---

## ✅ Validações Implementadas

| Campo | Regra | Código devolvido |
|---|---|---|
| Email | Obrigatório. Tem de conter `@` e `.` após o `@` | `400` |
| Data de nascimento | Formato `DD/MM/AAAA`. Ano entre 1900 e o ano atual | `400` |
| Modo do jogo | Tem de ser `single player`, `multiplayer` ou `ambos` | `400` |
| Idade mínima | Tem de ser um número inteiro | `400` |
| Tamanho (GB) | Tem de ser um número (pode ter decimais) | `400` |
| ID inexistente | ID não encontrado no dicionário | `404` |

---

## 🔁 Comportamento em Caso de Erro

As entidades **nunca têm `input()`** — apenas retornam o código de erro.
O `main.py` é responsável por mostrar a mensagem e repetir o pedido de dados:

* `400` ou `404` → o loop repete e pede os dados novamente
* `500` → mostra o erro e sai do loop

---

## ▶️ Como Executar o Projeto

1️⃣ Garantir que Python 3.6 ou superior está instalado

2️⃣ Executar no terminal:

```
python main.py
```

3️⃣ Utilizar o menu apresentado

> Não é necessário instalar nenhuma biblioteca externa.

---

## 📚 Conceitos Trabalhados

Este projeto permite consolidar:

* funções
* dicionários
* módulos Python
* importação entre ficheiros
* validação de dados
* estruturas condicionais
* ciclos `while`
* códigos de retorno (simulação de HTTP status codes)
* tratamento de erros com `try/except`

---

## 👨‍🏫 Utilização em Sala de Aula

Este projeto vai ser usado para:

* introdução ao CRUD
* exercícios guiados
* avaliação prática
* preparação para projetos maiores

---

## 📄 Licença Pedagógica

Projeto desenvolvido exclusivamente para fins educativos no curso **GPSI – 10.º ano**.
Pode ser reutilizado e adaptado livremente pelo professor e alunos.
