
from pathlib import Path

from sqlalchemy import create_engine, text


def montar_connection_string(tipo_banco, database):
    if tipo_banco.lower() == "sqlite":
        raiz_projeto = Path(__file__).resolve().parents[3]
        caminho_banco = Path(database)

        if not caminho_banco.is_absolute():
            caminho_banco = raiz_projeto / caminho_banco

        return f"sqlite:///{caminho_banco.as_posix()}"

    raise ValueError("Tipo de banco não suportado")


def criar_engine(connection_string):
    return create_engine(connection_string)


def executar_query(banco, query, parametros=None):
    with banco.connect() as conexao:
        resultado = conexao.execute(
            text(query),
            parametros or {}
        )
        return resultado.fetchall()


def registro_existe(banco, query, parametros=None):
    resultado = executar_query(banco, query, parametros)
    assert len(resultado) > 0, "Nenhum registro foi encontrado"


def contar_registros(banco, query, quantidade_esperada, parametros=None):
    resultado = executar_query(banco, query, parametros)
    assert len(resultado) == quantidade_esperada, (
        f"Esperado: {quantidade_esperada}; encontrado: {len(resultado)}"
    )


def validar_valor_coluna(
    banco, query, coluna, valor_esperado, parametros=None
):
    resultado = executar_query(banco, query, parametros)

    assert len(resultado) > 0, "Nenhum registro foi encontrado"

    nomes_colunas = resultado[0]._mapping.keys()
    assert coluna in nomes_colunas, f"Coluna '{coluna}' não encontrada"

    valor_obtido = resultado[0]._mapping[coluna]

    assert valor_obtido == valor_esperado, (
        f"Esperado: {valor_esperado}; encontrado: {valor_obtido}"
    )


def validar_resultado_esperado(banco, query, resultado_esperado):
    resultado = executar_query(banco, query)

    resultado_obtido = [list(linha) for linha in resultado]

    assert resultado_obtido == resultado_esperado, (
        f"Resultado esperado: {resultado_esperado}\n"
        f"Resultado obtido: {resultado_obtido}"
    )
