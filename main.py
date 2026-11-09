from fastapi import FastAPI
from pydantic import BaseModel, Field
from models import responder_pergunta

app = FastAPI(title="TP2 - Parte 2 - Q1 - Fake LLM", description="API de chatbot utilizando LangChain e Fake LLM.")

class ChatRequest(BaseModel):
    pergunta: str = Field(min_length=1)

class ChatResponse(BaseModel):
    pergunta: str
    resposta: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    resposta = responder_pergunta(request.pergunta)

    return ChatResponse(pergunta=request.pergunta, resposta=resposta)
