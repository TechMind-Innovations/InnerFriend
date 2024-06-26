from openai import OpenAI
import os
from dotenv import load_dotenv
from time import sleep
from app.utils.assistente_openai import *
from app.utils.selecionar_persona import * 
from app.utils.helpers import carrega
from app.utils.vision_inner_friend import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4o"
caminho_imagem_enviada = None
STATUS_COMPLETED = "completed" 
UPLOAD_FOLDER = 'dados' 
sinais_negativos = carrega('app/data/word_key.txt')


def bot(prompt, idade):
    global caminho_imagem_enviada
    maximo_tentativas = 2
    repeticao = 0
    assistente = pegar_json()
    thread_id = assistente["thread_id"]
    assistente_id = assistente["assistant_id"]
    
    while True:
        try:
            personalidade = retorno_personalidade(idade)

            cliente.beta.threads.messages.create(
                thread_id=thread_id, 
                role = "user",
                content =  f"""
                Assuma, de agora em diante, a personalidade abaixo. 
                Ignore as personalidades anteriores.

                # Persona
                {personalidade}
                """
            )

            resposta_vision = ""
            if caminho_imagem_enviada != None:
                 resposta_vision = analisar_imagem(caminho_imagem_enviada)
                 os.remove(caminho_imagem_enviada)
                 caminho_imagem_enviada = ""

            cliente.beta.threads.messages.create(
                thread_id=thread_id, 
                role = "user",
                content =  resposta_vision+prompt
            )
            
            run = cliente.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistente_id
            )

            while run.status != STATUS_COMPLETED:
                run = cliente.beta.threads.runs.retrieve(
                    thread_id=thread_id,
                    run_id=run.id
            )
            
            historico = list(cliente.beta.threads.messages.list(thread_id=thread_id).data)
            resposta = historico[0]
            print(historico)
            return resposta

        except Exception as erro:
                repeticao += 1
                if repeticao >= maximo_tentativas:
                        return "Erro no GPT: %s" % erro
                print('Erro de comunicação com OpenAI:', erro)
        sleep(1)
