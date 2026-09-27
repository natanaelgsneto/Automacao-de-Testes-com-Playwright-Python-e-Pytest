from pathlib import Path
import sys

pasta_page = Path(__file__).resolve().parent
sys.path.insert(0, str(pasta_page))
from utilities.comparador_de_arquivos import comparar_arquivos

comparar_arquivos(
    "base.txt",
    "atual.txt"
)