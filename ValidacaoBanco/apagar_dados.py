import sqlite3
from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
CAMINHO_BANCO = RAIZ_PROJETO / "stores" / "loja.db"

conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

# Apaga os pedidos primeiro, caso estejam relacionados aos usuários
cursor.execute("DELETE FROM pedidos")

# Apaga os usuários
cursor.execute("DELETE FROM usuarios")

conexao.commit()
conexao.close()

print("Dados apagados com sucesso!")