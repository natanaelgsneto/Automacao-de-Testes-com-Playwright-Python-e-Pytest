import sqlite3
from pathlib import Path

# Localiza a pasta principal do projeto
RAIZ_PROJETO = Path(__file__).resolve().parent

# Define a pasta e o arquivo do banco
PASTA_STORES = RAIZ_PROJETO / "stores"
PASTA_STORES.mkdir(exist_ok=True)

CAMINHO_BANCO = PASTA_STORES / "loja.db"

# Remove o arquivo anterior, caso exista
if CAMINHO_BANCO.exists():
    CAMINHO_BANCO.unlink()

# Cria um novo banco SQLite
conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

# Cria a tabela usuarios
cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    ativo INTEGER NOT NULL DEFAULT 1,
    data_cadastro TEXT NOT NULL
)
""")

# Cria a tabela produtos
cursor.execute("""
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
)
""")

# Cria a tabela pedidos
cursor.execute("""
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    total REAL NOT NULL
)
""")

conexao.commit()
conexao.close()

print("Tabelas criadas com sucesso!")
print("Banco:", CAMINHO_BANCO)