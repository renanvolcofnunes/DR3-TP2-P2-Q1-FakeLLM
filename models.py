from langchain_core.language_models.fake import FakeListLLM

respostas = {
    "oi": "Olá! Como posso ajudar?",
    "o que é fastapi?": "FastAPI é um framework Python para criar APIs.",
    "o que é langchain?": "LangChain é uma biblioteca para desenvolver aplicações com modelos de linguagem.",
    "o que é fake llm?": "Fake LLM simula respostas de um modelo para realizar testes."
}

def responder_pergunta(pergunta):
    resposta = respostas.get(pergunta.strip().lower(), "Desculpe, não tenho uma resposta para essa pergunta.")
    modelo = FakeListLLM(responses=[resposta])
    return modelo.invoke(pergunta)
