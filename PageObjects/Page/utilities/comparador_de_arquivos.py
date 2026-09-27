import os
import re
import tempfile
from pathlib import Path
from typing import Optional

import pandas as pd
import PyPDF2


# ==========================================================
# CAMINHOS DO PROJETO
# ==========================================================

# Local deste arquivo:
# PageObjects/Page/utilities/comparador_de_arquivos.py
#
# A pasta raiz será:
# PageObjects/

PASTA_PROJETO = Path(__file__).resolve().parents[2]
PASTA_ARQUIVOS = PASTA_PROJETO / "Arquivos"


# ==========================================================
# FUNÇÕES AUXILIARES
# ==========================================================

def contar_bytes_diferentes(texto_base: str, texto_atual: str) -> int:
    """
    Conta quantos bytes são diferentes entre dois textos.
    """
    bytes_base = texto_base.encode("utf-8")
    bytes_atual = texto_atual.encode("utf-8")

    diferencas = 0
    tamanho_maximo = max(len(bytes_base), len(bytes_atual))

    for indice in range(tamanho_maximo):
        byte_base = bytes_base[indice] if indice < len(bytes_base) else None
        byte_atual = bytes_atual[indice] if indice < len(bytes_atual) else None

        if byte_base != byte_atual:
            diferencas += 1

    return diferencas


def validar_arquivos(arquivo_base: str, arquivo_atual: str) -> None:
    """
    Verifica se os dois arquivos existem.
    """
    if not os.path.isfile(arquivo_base):
        raise FileNotFoundError(f"Arquivo base não encontrado: {arquivo_base}")

    if not os.path.isfile(arquivo_atual):
        raise FileNotFoundError(f"Arquivo atual não encontrado: {arquivo_atual}")


# ==========================================================
# COMPARAÇÃO DE ARQUIVOS DE TEXTO
# ==========================================================

def comparar_arquivos(
    arquivo_base: str,
    arquivo_atual: str,
    linhas_ignorar: Optional[list[int]] = None,
    padrao_ignorar: str = "",
    bytes_ignorar: int = 0,
    encoding: str = "utf-8",
) -> None:
    """
    Compara dois arquivos de texto linha por linha.

    linhas_ignorar:
        Lista de linhas que não devem ser comparadas.
        A numeração começa em 1.

    padrao_ignorar:
        Expressão regular que será removida antes da comparação.

    bytes_ignorar:
        Quantidade máxima de bytes diferentes permitida.
    """
    validar_arquivos(arquivo_base, arquivo_atual)

    if linhas_ignorar is None:
        linhas_ignorar = []

    with open(arquivo_base, "r", encoding=encoding) as arquivo1:
        linhas_base = arquivo1.readlines()

    with open(arquivo_atual, "r", encoding=encoding) as arquivo2:
        linhas_atual = arquivo2.readlines()

    if not linhas_atual:
        raise AssertionError("O arquivo atual está vazio.")

    if len(linhas_base) != len(linhas_atual):
        raise AssertionError("Os arquivos possuem quantidades diferentes de linhas.")

    total_bytes_diferentes = 0

    for indice, (linha_base, linha_atual) in enumerate(
        zip(linhas_base, linhas_atual), start=1
    ):
        if indice in linhas_ignorar:
            continue

        if padrao_ignorar:
            linha_base = re.sub(
                padrao_ignorar, "", linha_base, flags=re.DOTALL
            )
            linha_atual = re.sub(
                padrao_ignorar, "", linha_atual, flags=re.DOTALL
            )

        total_bytes_diferentes += contar_bytes_diferentes(
            linha_base, linha_atual
        )

    if total_bytes_diferentes > bytes_ignorar:
        raise AssertionError(
            f"Arquivos de texto diferentes. "
            f"Bytes diferentes: {total_bytes_diferentes}. "
            f"Tolerância: {bytes_ignorar}."
        )


# ==========================================================
# COMPARAÇÃO DE ARQUIVOS EXCEL
# ==========================================================

def comparar_arquivos_excel(
    arquivo_base: str,
    arquivo_atual: str,
    bytes_ignorar: int = 0,
    comparar_headers: bool = True,
) -> None:
    """
    Compara duas planilhas Excel célula por célula.

    Compara a primeira planilha de cada arquivo.

    bytes_ignorar:
        Quantidade máxima de bytes diferentes permitida.

    comparar_headers:
        Quando True, compara também os nomes das colunas.
    """
    validar_arquivos(arquivo_base, arquivo_atual)

    engine_base = (
        "xlrd" if arquivo_base.lower().endswith(".xls") else "openpyxl"
    )
    engine_atual = (
        "xlrd" if arquivo_atual.lower().endswith(".xls") else "openpyxl"
    )

    df_base = pd.read_excel(
        arquivo_base,
        engine=engine_base
    ).fillna("")

    df_atual = pd.read_excel(
        arquivo_atual,
        engine=engine_atual
    ).fillna("")

    if df_base.shape != df_atual.shape:
        raise AssertionError(
            "As planilhas possuem quantidades diferentes de linhas ou colunas."
        )

    total_bytes_diferentes = 0

    # Compara os cabeçalhos.
    if comparar_headers:
        headers_base = list(df_base.columns)
        headers_atual = list(df_atual.columns)

        if headers_base != headers_atual:
            total_bytes_diferentes += contar_bytes_diferentes(
                str(headers_base),
                str(headers_atual)
            )

    # Compara os valores das células.
    for linha in range(df_base.shape[0]):
        for coluna in range(df_base.shape[1]):
            valor_base = str(df_base.iat[linha, coluna])
            valor_atual = str(df_atual.iat[linha, coluna])

            if valor_base != valor_atual:
                total_bytes_diferentes += contar_bytes_diferentes(
                    valor_base,
                    valor_atual
                )

    if total_bytes_diferentes > bytes_ignorar:
        raise AssertionError(
            f"Planilhas Excel diferentes. "
            f"Bytes diferentes: {total_bytes_diferentes}. "
            f"Tolerância: {bytes_ignorar}."
        )


# ==========================================================
# CONVERSÃO DE PDF PARA TEXTO
# ==========================================================

def converter_pdf_para_texto(arquivo_pdf: str) -> str:
    """
    Extrai e normaliza o texto de um arquivo PDF.
    """
    validar_arquivos(arquivo_pdf, arquivo_pdf)

    paginas_texto = []

    try:
        with open(arquivo_pdf, "rb") as arquivo:
            leitor_pdf = PyPDF2.PdfReader(arquivo)

            for pagina in leitor_pdf.pages:
                texto = pagina.extract_text()

                if texto:
                    paginas_texto.append(texto)

    except Exception as erro:
        raise RuntimeError(
            f"Não foi possível ler o PDF: {arquivo_pdf}"
        ) from erro

    texto_completo = "\n".join(paginas_texto)
    texto_completo = texto_completo.replace("\r", "\n")
    texto_completo = re.sub(r"\n+", "\n", texto_completo)
    texto_completo = re.sub(r"[ \t]+", " ", texto_completo)

    return texto_completo.strip()


# ==========================================================
# CONVERSÃO E COMPARAÇÃO DE PDF
# ==========================================================

def converter_e_comparar_pdf(
    arquivo_base: str,
    arquivo_atual: str,
    linhas_ignorar: Optional[list[int]] = None,
    padrao_ignorar: str = "",
    bytes_ignorar: int = 0,
    encoding: str = "utf-8",
) -> None:
    """
    Extrai o texto de dois PDFs e compara o conteúdo.
    """
    validar_arquivos(arquivo_base, arquivo_atual)

    arquivo_temporario_base = None
    arquivo_temporario_atual = None

    try:
        texto_atual = converter_pdf_para_texto(arquivo_atual)

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".txt",
            encoding=encoding,
            delete=False
        ) as temporario:
            arquivo_temporario_atual = temporario.name
            temporario.write(texto_atual)

        if arquivo_base.lower().endswith(".pdf"):
            texto_base = converter_pdf_para_texto(arquivo_base)

            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=".txt",
                encoding=encoding,
                delete=False
            ) as temporario:
                arquivo_temporario_base = temporario.name
                temporario.write(texto_base)

            base_para_comparar = arquivo_temporario_base
        else:
            base_para_comparar = arquivo_base

        comparar_arquivos(
            arquivo_base=base_para_comparar,
            arquivo_atual=arquivo_temporario_atual,
            linhas_ignorar=linhas_ignorar,
            padrao_ignorar=padrao_ignorar,
            bytes_ignorar=bytes_ignorar,
            encoding=encoding,
        )

    finally:
        if arquivo_temporario_atual and os.path.exists(
            arquivo_temporario_atual
        ):
            os.remove(arquivo_temporario_atual)

        if arquivo_temporario_base and os.path.exists(
            arquivo_temporario_base
        ):
            os.remove(arquivo_temporario_base)

# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == "__main__":
    print("Iniciando comparação dos arquivos Excel...")

    comparar_arquivos_excel(
        arquivo_base=str(PASTA_ARQUIVOS / "base.xlsx"),
        arquivo_atual=str(PASTA_ARQUIVOS / "atual.xlsx"),
    )

    print("Comparação concluída: as planilhas são iguais!")