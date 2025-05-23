from agent.groq_agent import iniciar_agente

def main():
  print("\n=== Analisador de Dados de Transplantes ===\n")
  pergunta = input("Digite sua pergunta sobre a base de transplantes: ")
  resposta = iniciar_agente(pergunta)
  print("\nResposta do assistente:\n")
  print(resposta)

if __name__ == "__main__":
  main()