import sqlite3
from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
CAMINHO_BANCO = RAIZ_PROJETO / "stores" / "loja.db"

conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

cursor.executemany(
    """
    INSERT INTO usuarios (nome, email, ativo, data_cadastro)
    VALUES (?, ?, ?, ?)
    """,
    [
        ("Joao Silva", "joao@teste.com", 1, "2026-01-10"),
        ("Maria Souza", "maria@teste.com", 1, "2026-01-12"),
        ("Carlos Lima", "carlos@teste.com", 0, "2026-01-15"),
    ],
)

cursor.executemany(
    """
    INSERT INTO produtos (nome, preco, estoque)
    VALUES (?, ?, ?)
    """,
    [
        ("Camiseta Preta", 79.90, 50),
        ("Calca Jeans", 199.90, 20),
        ("Tenis Esportivo", 349.90, 10),
    ],
)

cursor.executemany(
    """
    INSERT INTO pedidos (usuario_id, produto_id, quantidade, total)
    VALUES (?, ?, ?, ?)
    """,
    [
        (1, 1, 2, 159.80),
        (2, 3, 1, 349.90),
    ],
)

conexao.commit()
conexao.close()

print("Dados inseridos com sucesso!")