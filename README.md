# 🎮 Projeto Gestor de Steam - CRUD

## 📘 Descrição do Projeto

Este projeto foi desenvolvido com fins pedagógicos para alunos do **Curso Profissional de Gestão e Programação de Sistemas Informáticos (GPSI) – 10.º ano**.

O objetivo principal é demonstrar como implementar operações **CRUD (Create, Read, Update, Delete)** em Python utilizando:

* funções (sem classes)
* dicionários
* separação por ficheiros
* validação de dados
* menus em terminal

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

---

## 📂 Estrutura do Projeto

```
.
└── gestor_steam/
     ├── main.py
     ├── utilizador.py
     ├── jogo.py
     ├── utils.py
     └── README.md
```

### main.py
Contém o **menu interativo em terminal**.
Responsável apenas por:

* apresentar opções ao utilizador
* recolher dados introduzidos
* chamar funções dos módulos `utilizador` e `jogo`

Não contém validações — essas ficam nos respetivos módulos.

---

### utilizador.py
Contém todas as operações CRUD da entidade **Utilizador**:

* criar utilizador
* listar utilizadores
* consultar utilizador
* atualizar utilizador
* remover utilizador

Inclui validações como verificação de email, datas e geração automática de ID.  
Os utilizadores são guardados num **dicionário em memória**.

---

### jogo.py
Contém todas as operações CRUD da entidade **Jogo**:

* criar jogo
* listar jogos
* consultar jogo
* atualizar jogo
* remover jogo

Inclui validações de modo, idade mínima e tamanho.  
Os jogos são guardados num **dicionário em memória**.

---

### utils.py
Contém funções auxiliares partilhadas por todos os módulos:

* geração automática de IDs no formato `U001`, `J001`, ...
* validação de datas no formato `DD/MM/AAAA`
* validação de email

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

## ✅ Validações Implementadas

| Campo | Regra |
|---|---|
| Email | Obrigatório. Tem de conter `@` e `.` após o `@` |
| Data de nascimento | Formato `DD/MM/AAAA`. Ano entre 1900 e o ano atual |
| Modo do jogo | Tem de ser `single player`, `multiplayer` ou `ambos` |
| Idade mínima | Tem de ser um número inteiro |
| Tamanho (GB) | Tem de ser um número (pode ter decimais) |
| ID (consultar/atualizar/remover) | Fica em loop até introduzir um ID existente |

---

## 🔁 Comportamento em Caso de Erro

O programa **nunca volta ao menu** quando ocorre um erro de validação.  
Em vez disso, fica em loop e pede novamente o valor até ser válido.

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
