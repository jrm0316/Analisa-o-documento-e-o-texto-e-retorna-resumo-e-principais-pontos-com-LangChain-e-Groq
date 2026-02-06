# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE_DIR, "dados.txt")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

with open(ARQUIVO, "r", encoding="utf-8") as f:
    texto = f.read()

prompt = PromptTemplate(
    input_variables=["texto"],
    template="""
    Analise o texto abaixo e retorne:
    - Resumo
    - Principais pontos

    Texto:
    {texto}
    """
)

prompt_final = prompt.format(texto=texto)
resposta = llm.invoke(prompt_final)

print(resposta.content)