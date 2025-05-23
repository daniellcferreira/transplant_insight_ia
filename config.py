# config.py
import os
from dotenv import load_dotenv

def carregar_api_key():
  """
  Carrega a chave da API Groq do arquivo .env
  """
  load_dotenv()
  os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")