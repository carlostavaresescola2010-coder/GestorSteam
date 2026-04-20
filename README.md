# 🎮 Gestor de Steam

Aplicação de terminal em Python para gerir utilizadores e jogos, com armazenamento em memória e validações ao estilo de uma API HTTP.

---

## 📁 Estrutura do Projeto

```
.
├── main.py           # Ponto de entrada — menus e interação com o utilizador
├── utilizadores.py   # CRUD da entidade Utilizador
├── jogos.py          # CRUD da entidade Jogo
└── utils.py          # Funções auxiliares partilhadas (IDs, validações)
```

---

## ▶️ Como Executar

```bash
python main.py
```

Não são necessárias dependências externas — usa apenas a biblioteca padrão do Python.

---

## ✨ Funcionalidades

### Utilizadores
- **Criar** — regista um novo utilizador com nome, username, email, password e data de nascimento
- **Listar** — mostra todos os utilizadores registados
- **Consultar** — apresenta os detalhes de um utilizador pelo ID (password mascarada com `*`)
- **Atualizar** — edita campos individualmente (campos em branco mantêm o valor atual)
- **Remover** — elimina um utilizador pelo ID

### Jogos
- **Criar** — regista um novo jogo com nome, modo, idade mínima e tamanho em GB
- **Listar** — mostra todos os jogos registados
- **Consultar** — apresenta os detalhes de um jogo pelo ID
- **Atualizar** — edita campos individualmente
- **Remover** — elimina um jogo pelo ID

---

## 🗂️ Formato dos IDs

Os IDs são gerados automaticamente e incrementados a cada criação:

| Entidade     | Formato | Exemplo |
|--------------|---------|---------|
| Utilizador   | `UXXX`  | `U001`  |
| Jogo         | `JXXX`  | `J001`  |

---

## ✅ Validações

### Utilizador
| Campo       | Regra                                              |
|-------------|----------------------------------------------------|
| Email       | Obrigatório, deve conter `@` e `.` após o `@`     |
| Nascimento  | Formato `DD/MM/AAAA`, ano entre 1900 e o atual    |

### Jogo
| Campo         | Regra                                                  |
|---------------|--------------------------------------------------------|
| Modo          | Um de: `single player`, `multiplayer`, `ambos`        |
| Idade mínima  | Número inteiro                                         |
| Tamanho (GB)  | Número (aceita decimais)                               |

---

## 📡 Códigos de Retorno

Cada função de CRUD retorna um tuplo `(código, dados)` ao estilo HTTP:

| Código | Significado                        |
|--------|------------------------------------|
| `200`  | Operação bem-sucedida              |
| `201`  | Recurso criado com sucesso         |
| `400`  | Dados inválidos (erro de validação)|
| `404`  | Recurso não encontrado             |
| `500`  | Erro interno inesperado            |

---

## 🔧 Detalhes Técnicos

- **Armazenamento:** dicionários em memória (os dados não persistem entre execuções)
- **Arquitetura:** separação clara entre lógica de negócio (`utilizadores.py`, `jogos.py`), utilitários (`utils.py`) e interface (`main.py`)
- **Navegação:** loops nos menus repetem o pedido em caso de erro `400` ou `404`, e saem em caso de erro `500`
- **Compatibilidade:** o ecrã é limpo com `cls` no Windows e `clear` no Linux/macOS
