# 🎮 Gestor de Steam

Sistema de gestão de uma plataforma de jogos, desenvolvido em Python. Permite gerir utilizadores, jogos, loja e compras através de um menu interativo no terminal.

---

## 📁 Estrutura do Projeto

```
.
├── main.py           # Ponto de entrada — menus e interação com o utilizador
├── utilizadores.py   # CRUD da entidade Utilizador
├── jogos.py          # CRUD da entidade Jogo
├── loja.py           # CRUD da entidade Loja
├── compra.py         # CRUD da entidade Compra
└── utils.py          # Funções auxiliares (IDs, validações)
```

---

## ▶️ Como Executar

Não é necessária nenhuma dependência externa. Apenas Python 3.x.

```bash
python main.py
```

---

## 🗂️ Entidades

### 👤 Utilizador
Representa um utilizador registado na plataforma.

| Campo       | Tipo   | Descrição                        |
|-------------|--------|----------------------------------|
| `uid`       | str    | ID gerado automaticamente (U001) |
| `nome`      | str    | Nome completo                    |
| `username`  | str    | Nome de utilizador               |
| `email`     | str    | Endereço de email (validado)     |
| `password`  | str    | Palavra-passe                    |
| `nascimento`| str    | Data de nascimento (DD/MM/AAAA)  |

---

### 🎮 Jogo
Representa um jogo disponível na plataforma.

| Campo          | Tipo   | Descrição                           |
|----------------|--------|-------------------------------------|
| `jid`          | str    | ID gerado automaticamente (J001)    |
| `nome`         | str    | Nome do jogo                        |
| `modo`         | str    | `single player`, `multiplayer` ou `ambos` |
| `idade_minima` | int    | Idade mínima recomendada            |
| `tamanho_gb`   | float  | Tamanho em gigabytes                |

---

### 🏪 Loja
Representa um jogo disponível para compra, com preço e stock.

| Campo   | Tipo   | Descrição                        |
|---------|--------|----------------------------------|
| `lid`   | str    | ID gerado automaticamente (L001) |
| `jid`   | str    | Referência ao jogo               |
| `preco` | float  | Preço em euros (≥ 0)             |
| `stock` | int    | Unidades disponíveis (≥ 0)       |

> Cada jogo só pode ter **uma entrada** na loja.

---

### 🛒 Compra
Representa a transação de um utilizador ao adquirir um jogo da loja.

| Campo        | Tipo   | Descrição                          |
|--------------|--------|------------------------------------|
| `cid`        | str    | ID gerado automaticamente (C001)   |
| `uid`        | str    | Referência ao utilizador           |
| `lid`        | str    | Referência ao item da loja         |
| `data_compra`| str    | Data da compra (DD/MM/AAAA)        |
| `preco_pago` | float  | Preço fixado no momento da compra  |

> O `preco_pago` é registado no momento da compra e **não é alterado** se o preço da loja mudar posteriormente.  
> Ao remover uma compra, o stock do respetivo item é **devolvido automaticamente**.

---

## ✅ Validações

Todas as validações são feitas nas camadas de CRUD (nunca no `main.py`).

| Campo        | Regra                                                        |
|--------------|--------------------------------------------------------------|
| Email        | Deve conter `@` e um `.` após o `@`                         |
| Data         | Formato `DD/MM/AAAA`, ano entre 1900 e o ano atual          |
| Modo de jogo | Um de: `single player`, `multiplayer`, `ambos`              |
| Preço        | Número decimal, não pode ser negativo                        |
| Stock        | Número inteiro, não pode ser negativo                        |
| Idade mínima | Número inteiro                                               |

---

## 📡 Códigos de Retorno (estilo HTTP)

Todas as funções de CRUD retornam um tuplo `(código, dados)`.

| Código | Significado                              |
|--------|------------------------------------------|
| `200`  | Operação realizada com sucesso           |
| `201`  | Registo criado com sucesso               |
| `400`  | Erro de validação nos dados fornecidos   |
| `404`  | Registo não encontrado                   |
| `500`  | Erro interno inesperado                  |

---

## 💾 Armazenamento

Os dados são guardados **em memória** (dicionários Python) durante a execução do programa. Ao terminar, todos os dados são perdidos — não existe persistência em ficheiro ou base de dados.

---

## 🔑 Geração de IDs

Os IDs são gerados automaticamente e sequencialmente, com prefixo por entidade:

| Entidade    | Formato | Exemplo |
|-------------|---------|---------|
| Utilizador  | `Unnn`  | `U001`  |
| Jogo        | `Jnnn`  | `J001`  |
| Loja        | `Lnnn`  | `L001`  |
| Compra      | `Cnnn`  | `C001`  |

Os contadores são globais e incrementam a cada criação, independentemente de remoções anteriores.
