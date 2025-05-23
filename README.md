# Analisador de Dados de Transplantes

[![Python](https://img.shields.io/badge/Python-Linguagem-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=flat-square)](https://python.langchain.com/en/latest/)
[![Groq API](https://img.shields.io/badge/Groq-API%20LLM-purple?style=flat-square)](https://groq.ai/)
[![Pandas](https://img.shields.io/badge/Pandas-Análise%20Dados-blue?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)


---

## Descrição

Este projeto consiste em um sistema interativo para análise de dados de transplantes utilizando técnicas de inteligência artificial com LangChain e Groq. Através de um agente programado, o usuário pode realizar perguntas em linguagem natural sobre um conjunto de dados em formato CSV, que são automaticamente convertidas em comandos Python executados sobre um DataFrame Pandas. O sistema responde com resultados precisos de operações estatísticas como média, máximo, mínimo e muito mais.

---

## Funcionalidades

- Carregamento dinâmico de base de dados em formato CSV contendo dados de transplantes.
- Processamento de perguntas em linguagem natural sobre os dados.
- Conversão automática das perguntas para código Python que consulta o DataFrame Pandas.
- Resposta rápida com métricas estatísticas (média, máximo, mínimo, contagem, etc).
- Interface simples em terminal para interação direta.
- Uso da API Groq para suporte ao modelo LLM com LangChain.
- Tratamento de erros e controle de iterações para garantir estabilidade.

---

## Tecnologias Abordadas

- **Python 3.11:** Linguagem principal para desenvolvimento do projeto, incluindo manipulação de dados e integração com APIs.
- **Pandas:** Biblioteca essencial para manipulação e análise de dados tabulares em DataFrames.
- **LangChain:** Framework para criação de agentes inteligentes que interpretam linguagem natural e executam ações programadas.
- **Groq API:** Plataforma que oferece modelos de linguagem de última geração para processamento de texto e geração de código.

---
