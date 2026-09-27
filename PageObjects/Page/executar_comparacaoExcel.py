from pathlib import Path
import sys

pasta_page = Path(__file__).resolve().parent
sys.path.insert(0, str(pasta_page))

from utilities.comparador_de_arquivos import comparar_arquivos_excel

comparar_arquivos_excel(
    "base.xlsx",
    "atual.xlsx"
)

#para rodar digite python -c "import pandas as pd; print('BASE:'); print(pd.read_excel('base.xlsx')); print('ATUAL:'); print(pd.read_excel('atual.xlsx'))"
