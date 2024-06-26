from gc import set_debug
from openai import OpenAI
from dotenv import load_dotenv
import os
from app.utils.helpers import carrega
from app.utils.selecionar_persona import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-3.5-turbo"
sinais_negativos = carrega('app/data/word_key.txt')

def criar_assistente(idade_usuario: int):
    chave_personalidade = selecionar_persona(idade_usuario)
    if chave_personalidade is None:
        raise ValueError("Idade do usuário fora do intervalo suportado.")
    
    descricao_personalidade = personas.get(chave_personalidade)
    if descricao_personalidade is None:
        raise ValueError("Descrição da personalidade não encontrada.")
    
    assistente = cliente.beta.assistants.create(
        name="Inner Friend",
        instructions = f"""
                Você é um amigo íntimo do usuário em que ele confia para falar sobre seu dia a dia.
                Você deve ser mais compreensivo, humano e utilizando mensagens curtas, apenas em casos que identificar sinais contra risco a vida use mensagens longas.
                Você deve entender como sinais negativos, os sinais abaixo.
                Além disso, adote a persona abaixo para responder ao cliente.

            ##Sinais negativos de morte
            {sinais_negativos}

             ##Persona
            {personas[chave_personalidade]}
        """,
        model = modelo,
    )
    return assistente

def criar_thread():
    cliente.beta.threads.create()
