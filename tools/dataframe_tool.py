from langchain.agents import tool
import pandas as pd

def dataframe_tool(df: pd.DataFrame):

  @tool
  def analisar_dados(pergunta: str) -> str:
    """
    Executa análise exploratória sobre um DataFrame de dados de transplantes.
    A pergunta pode envolver filtros, agrupamentos, estatísticas, etc.
    """
    try:
      # Código seguro para avaliação de operações sobre o DataFrame
      import io
      import contextlib

      buffer = io.StringIO()
      with contextlib.redirect_stdout(buffer):
        exec(pergunta, {"df": df, "pd": pd})

      return buffer.getvalue()
    except Exception as e:
      return f"Erro ao analisar dados: {e}"

  return analisar_dados