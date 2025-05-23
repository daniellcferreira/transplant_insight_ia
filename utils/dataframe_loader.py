import pandas as pd

def carregar_dataframe(caminho_csv: str) -> pd.DataFrame:
  """
  Carrega o DataFrame do CSV informado.
  """
  return pd.read_csv(caminho_csv, sep=';')
