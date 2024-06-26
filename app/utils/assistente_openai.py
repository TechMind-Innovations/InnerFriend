import json
from openai import OpenAI
from dotenv import load_dotenv
import os
from app.utils.helpers import carrega
from app.utils.selecionar_persona import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4o"
sinais_negativos = carrega('app/data/word_key.txt')

def criar_lista_ids():
    lista_ids_arquivos = []
    file_palavras_chave = cliente.files.create(
        file = open('app/data/word_key.txt', "rb"),
        purpose = "assistants"
    )
    lista_ids_arquivos.append(file_palavras_chave.id)
    return lista_ids_arquivos

def pegar_json():
    filename = "assistentes.json"
    
    if not os.path.exists(filename):
        thread_id = criar_thread()
        file_id_list = criar_lista_ids()
        assistant_id = criar_assistente(file_id_list)
        data = {
            "assistant_id": assistant_id.id,
            "thread_id": thread_id.id,
            "file_ids": file_id_list
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Arquivo 'assistentes.json' criado com sucesso.")
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Arquivo 'assistentes.json' não encontrado.")

def criar_thread():
    return cliente.beta.threads.create()

def criar_assistente(file_ids = []):
    assistente = cliente.beta.assistants.create(
        name="Inner Friend",
        instructions = f"""
                Você é um amigo íntimo do usuário em que ele confia para falar sobre seu dia a dia.
                Você deve ser mais compreensivo, humano e utilizando mensagens curtas, apenas em casos que identificar sinais contra risco a vida use mensagens longas.
                Além disso, acesse os arquivos associados a você e a thread para responder as perguntas.
                """,
        model = modelo,
    )
    return assistente
