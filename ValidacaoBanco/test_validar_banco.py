
from PageObjects.Page.utilities.bancosDeDados import (
    criar_engine,
    montar_connection_string,
    registro_existe,
    contar_registros,
    validar_valor_coluna,
    validar_resultado_esperado,
)


def criar_banco():
    url = montar_connection_string(
        "sqlite",
        database="stores/loja.db",
    )
    return criar_engine(url)


def test_usuario_existe():
    banco = criar_banco()

    query = "SELECT * FROM usuarios WHERE email = :email"
    parametros = {"email": "joao@teste.com"}

    registro_existe(banco, query, parametros)


def test_contar_usuarios_ativos():
    banco = criar_banco()

    query = "SELECT * FROM usuarios WHERE ativo = 1"

    contar_registros(
        banco,
        query,
        quantidade_esperada=2,
    )


def test_validar_preco_produto():
    banco = criar_banco()

    query = "SELECT nome, preco FROM produtos WHERE nome = :nome"
    parametros = {"nome": "Calca Jeans"}

    validar_valor_coluna(
        banco,
        query,
        coluna="preco",
        valor_esperado=199.90,
        parametros=parametros,
    )


def test_validar_lista_produtos():
    banco = criar_banco()

    query = "SELECT nome, estoque FROM produtos ORDER BY id"

    produtos_esperados = [
        ["Camiseta Preta", 50],
        ["Calca Jeans", 20],
        ["Tenis Esportivo", 10],
    ]

    validar_resultado_esperado(
        banco,
        query,
        produtos_esperados,
    )
#EXECUTE
# EXECUTE python -c "import sqlite3; c=sqlite3.connect('stores/loja.db'); c.execute('DELETE FROM produtos WHERE id IN (4,5,6)'); c.commit(); print(c.execute('SELECT id, nome, estoque FROM produtos ORDER BY id').fetchall()); c.close()" NA pasta  (.venv) PS C:\Users\Natan\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest>
# o resultado deve ser: 