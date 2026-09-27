

"""
Exemplos da aula: Utilitário para Validação de Banco de Dados.

Demonstra funções de Page/utilitarios/bancos_dados.py
contra o banco de exemplo loja.db (SQLite), na raiz do projeto.

Pré-requisito:
    O arquivo stores/loja.db deve existir e conter as tabelas
    usuarios e produtos.

Execução:
    python PageObjects/Tests/Treinamento/testes_banco_dados.py
"""

import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Caminhos do projeto
# ---------------------------------------------------------------------------

# Este arquivo está em:
# projeto/PageObjects/Tests/Treinamento/testes_banco_dados.py
#
# parents[0] = .../PageObjects/Tests/Treinamento
# parents[1] = .../PageObjects/Tests
# parents[2] = .../PageObjects
# parents[3] = raiz do projeto

PASTA_PAGEOBJECTS = Path(__file__).resolve().parents[2]
RAIZ_PROJETO = PASTA_PAGEOBJECTS.parent

# Permite importar o pacote Page mesmo quando o script é executado
# diretamente pelo terminal ou pelo PyCharm.
if str(PASTA_PAGEOBJECTS) not in sys.path:
    sys.path.insert(0, str(PASTA_PAGEOBJECTS))

from Page.utilitarios.bancos_dados import (
    atualizar,
    contar_registros,
    criar_engine,
    executar_comando,
    executar_query,
    imprimir_resultado,
    inserir,
    montar_connection_string,
    registro_existe,
    registro_nao_existe,
    salvar_resultado_em_arquivo,
    validar_resultado_esperado,
    validar_valor_coluna,
)

# Caminho absoluto para o banco SQLite.
CAMINHO_BANCO = RAIZ_PROJETO / "stores" / "loja.db"

# Massa de dados usada nos exemplos de INSERT, UPDATE e DELETE.
EMAIL_TESTE = "ana@teste.com"


def titulo(texto):
    """Imprime um cabeçalho para separar os blocos no console."""
    print(f"\n{'=' * 60}\n{texto}\n{'=' * 60}")


# ---------------------------------------------------------------------------
# 1. Conexão
# ---------------------------------------------------------------------------

def exemplo_conexao():
    """Monta a connection string e cria a engine do SQLAlchemy."""
    titulo("1. CONEXÃO")

    if not CAMINHO_BANCO.exists():
        raise FileNotFoundError(
            f"Banco de dados não encontrado: {CAMINHO_BANCO}\n"
            "Verifique se o script de criação do banco já foi executado."
        )

    connection_string = montar_connection_string(
        "sqlite",
        database=str(CAMINHO_BANCO),
    )

    print(f"Banco utilizado: {CAMINHO_BANCO}")
    print(f"Connection string: {connection_string}")

    return criar_engine(connection_string)


# ---------------------------------------------------------------------------
# 2. Consultando dados
# ---------------------------------------------------------------------------

def exemplo_consulta(engine):
    """Lê dados do banco e exibe o resultado formatado."""
    titulo("2. CONSULTANDO DADOS")

    print("Tabela usuarios:")
    imprimir_resultado(
        engine,
        "SELECT id, nome, email, ativo FROM usuarios",
    )

    print("\nTabela produtos:")
    imprimir_resultado(
        engine,
        "SELECT id, nome, preco, estoque FROM produtos",
    )

    # executar_query devolve (colunas, linhas) para uso direto no código.
    colunas, linhas = executar_query(
        engine,
        "SELECT nome, preco FROM produtos",
    )

    print(f"\nColunas: {colunas}")

    if linhas:
        print(f"Primeira linha: {linhas[0]}")
    else:
        print("A consulta não retornou produtos.")


# ---------------------------------------------------------------------------
# 3. Validadores
# ---------------------------------------------------------------------------

def exemplo_validadores(engine):
    """Demonstra os validadores do utilitário."""
    titulo("3. VALIDADORES")

    # Existe ao menos um registro?
    registro_existe(
        engine,
        "SELECT * FROM usuarios WHERE email = :email",
        {"email": "joao@teste.com"},
    )

    # Não existe nenhum registro?
    registro_nao_existe(
        engine,
        "SELECT * FROM usuarios WHERE email = :email",
        {"email": "naoexiste@teste.com"},
    )

    # Quantidade exata de registros.
    contar_registros(
        engine,
        "SELECT * FROM usuarios WHERE ativo = 1",
        2,
    )

    # Valor de uma coluna específica.
    validar_valor_coluna(
        engine,
        "SELECT nome, preco FROM produtos WHERE nome = :nome",
        "preco",
        199.90,
        {"nome": "Calca Jeans"},
    )

    # Resultado completo comparado com um gabarito.
    validar_resultado_esperado(
        engine,
        "SELECT nome, estoque FROM produtos ORDER BY id",
        [
            ["Camiseta Preta", 50],
            ["Calca Jeans", 20],
            ["Tenis Esportivo", 10],
        ],
    )


# ---------------------------------------------------------------------------
# 4. Quando a validação falha
# ---------------------------------------------------------------------------

def exemplo_validacao_falha(engine):
    """Mostra a mensagem de erro quando um validador não passa."""
    titulo("4. QUANDO A VALIDAÇÃO FALHA")

    try:
        contar_registros(
            engine,
            "SELECT * FROM usuarios WHERE ativo = 1",
            5,
        )
    except AssertionError as erro:
        print(f"AssertionError: {erro}")


# ---------------------------------------------------------------------------
# 5. Escrita: massa de dados e limpeza
# ---------------------------------------------------------------------------

def exemplo_escrita(engine):
    """Demonstra INSERT, UPDATE e DELETE."""
    titulo("5. ESCRITA (INSERT / UPDATE / DELETE)")

    # INSERT - cria a massa de dados.
    linhas = inserir(
        engine,
        "usuarios",
        {
            "nome": "Ana Prova",
            "email": EMAIL_TESTE,
            "ativo": 1,
            "data_cadastro": "2026-02-01",
        },
    )

    print(f"Registros inseridos: {linhas}")

    registro_existe(
        engine,
        "SELECT * FROM usuarios WHERE email = :email",
        {"email": EMAIL_TESTE},
    )

    # UPDATE - altera o usuário criado.
    linhas = atualizar(
        engine,
        "usuarios",
        {"ativo": 0},
        "email = :email",
        {"email": EMAIL_TESTE},
    )

    print(f"\nRegistros atualizados: {linhas}")

    validar_valor_coluna(
        engine,
        "SELECT ativo FROM usuarios WHERE email = :email",
        "ativo",
        0,
        {"email": EMAIL_TESTE},
    )

    # DELETE - remove a massa de dados criada pelo exemplo.
    linhas = executar_comando(
        engine,
        "DELETE FROM usuarios WHERE email = :email",
        {"email": EMAIL_TESTE},
    )

    print(f"\nRegistros removidos: {linhas}")

    registro_nao_existe(
        engine,
        "SELECT * FROM usuarios WHERE email = :email",
        {"email": EMAIL_TESTE},
    )


# ---------------------------------------------------------------------------
# 6. Rollback automático
# ---------------------------------------------------------------------------

def exemplo_rollback(engine):
    """Demonstra o tratamento de uma operação inválida."""
    titulo("6. ROLLBACK AUTOMÁTICO")

    _, linhas = executar_query(
        engine,
        "SELECT * FROM usuarios",
    )

    total_antes = len(linhas)
    print(f"Usuários antes do comando inválido: {total_antes}")

    try:
        executar_comando(
            engine,
            "INSERT INTO usuarios (coluna_inexistente) VALUES (1)",
        )
    except Exception as erro:
        print(f"Erro capturado: {type(erro).__name__}")

    # Confere se a quantidade de usuários permaneceu igual.
    contar_registros(
        engine,
        "SELECT * FROM usuarios",
        total_antes,
    )


# ---------------------------------------------------------------------------
# 7. Exportando o resultado para arquivo
# ---------------------------------------------------------------------------

def exemplo_exportar_arquivo(engine):
    """Salva o resultado de uma consulta em um arquivo .txt."""
    titulo("7. EXPORTANDO RESULTADO PARA ARQUIVO")

    destino = RAIZ_PROJETO / "stores" / "produtos_atual.txt"
    destino.parent.mkdir(parents=True, exist_ok=True)

    salvar_resultado_em_arquivo(
        engine,
        "SELECT id, nome, preco FROM produtos ORDER BY id",
        str(destino),
    )

    print(f"Arquivo gerado: {destino}\n")
    print(destino.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Limpeza de massa residual
# ---------------------------------------------------------------------------

def limpar_massa_residual(engine):
    """
    Remove a massa de teste de execuções anteriores.

    Atenção: remove qualquer usuário com o e-mail EMAIL_TESTE.
    """
    executar_comando(
        engine,
        "DELETE FROM usuarios WHERE email = :email",
        {"email": EMAIL_TESTE},
    )


# ---------------------------------------------------------------------------
# Execução principal
# ---------------------------------------------------------------------------

def main():
    """Executa os exemplos da aula em sequência."""
    engine = exemplo_conexao()

    try:
        limpar_massa_residual(engine)

        exemplo_consulta(engine)
        exemplo_validadores(engine)
        exemplo_validacao_falha(engine)
        exemplo_escrita(engine)
        exemplo_rollback(engine)
        exemplo_exportar_arquivo(engine)

        titulo("FIM - exemplos executados")

    finally:
        engine.dispose()


if __name__ == "__main__":
    main()
##para mostrar os registros execute: .\.venv\Scripts\python.exe -c "import sqlite3; c=sqlite3.connect('stores/loja.db'); print(*c.execute('SELECT id, nome, preco, estoque FROM produtos ORDER BY id').fetchall(), sep='\n'); c.close()"