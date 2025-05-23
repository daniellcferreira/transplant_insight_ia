import pandas as pd
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from tools.dataframe_tool import dataframe_tool
from prompts.react_prompt import prompt_template

def iniciar_agente(pergunta: str) -> str:
  df = pd.read_csv("data/transplantes_brasil.csv", sep=';')
  llm = ChatGroq(model="llama3-70b-8192")
  analisar_dataframe = dataframe_tool(df)
  ferramentas = [analisar_dataframe]

  agente = initialize_agent(
    ferramentas,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    prompt=prompt_template,
    verbose=True,
    handle_parsing_errors=True
  )

  resposta = agente.run(pergunta)
  return resposta
