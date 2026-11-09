# Parte 2 - Q1 - Fake LLM

## Descricao
Chatbot com respostas simuladas utilizando LangChain.

## Requisitos
Python 3.14 e dependencias listadas em requirements.txt.

## Instalacao
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt

## Execucao
    python -m uvicorn main:app --reload --port 8002

## Documentacao da API
http://127.0.0.1:8002/docs

## Endpoint
POST /chat

## Exemplo de requisicao
    {"pergunta":"oi"}

## Observacoes
Utiliza FakeListLLM com respostas predefinidas.
