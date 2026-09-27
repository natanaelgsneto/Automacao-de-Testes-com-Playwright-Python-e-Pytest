from pathlib import Path

from sqlalchemy import create_engine, text

# Localiza o banco SQLite
RAIZ_PROJETO = Path(__file__).resolve().parent
CAMINHO_BANCO = RAIZ_PROJETO / "stores" / "loja.db"

# Cria a conexão com o banco
engine = create_engine(
    f"sqlite:///{CAMINHO_BANCO.as_posix()}"
)

# Consulta os usuários
with engine.connect() as conexao:
    resultado = conexao.execute(
        text("SELECT id, nome, email, ativo FROM usuarios")
    )

    usuarios = resultado.fetchall()

    print("Usuários encontrados:")
    for usuario in usuarios:
        print(usuario)

    # Valida se o usuário existe
    usuario_encontrado = conexao.execute(
        text("""
            SELECT id
            FROM usuarios
            WHERE email = :email
        """),
        {"email": "joao@teste.com"},
    ).fetchone()

    assert usuario_encontrado is not None, (
        "O usuário joao@teste.com não foi encontrado!"
    )

    print("VALIDAÇÃO OK: usuário encontrado no banco!")