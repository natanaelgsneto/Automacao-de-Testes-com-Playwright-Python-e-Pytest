
from PageObjects.Page.utilitarios.bancos_dados import (
    contar_registros,
    criar_engine,
)


def test_contar_registros():
    engine = criar_engine("sqlite:///:memory:")

    try:
        contar_registros(engine, "SELECT 1", 1)
    finally:
        engine.dispose()
