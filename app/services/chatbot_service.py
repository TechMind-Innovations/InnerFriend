import openai
import os
from dotenv import load_dotenv
from time import sleep
from app.utils.assistente_openai import *
from app.utils.selecionar_persona import * 

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-3.5-turbo"

def bot(prompt, idade):
    assistente = criar_assistente(idade)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": assistente},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Erro no GPT: {str(e)}"

# def bot(prompt, idade):
#     maximo_tentativas = 2
#     repeticao = 0
#     assistente = criar_assistente(idade)
#     thread = criar_thread()
    
#     while True:
#         try:
#             cliente.beta.threads.messages.create(
#                  thread_id = thread.id,
#                  role = "user",
#                  content = prompt
#             )

#             run = cliente.beta.threads.runs.create(
#                  thread_id = thread.id,
#                  assistant_id = assistente.id 
#             )
        
#             while run.status != "completed":
#                 run = cliente.beta.threads.runs.create(
#                     thread_id = thread.id,
#                     run_id = run.id
#             )
            
#             historico = list(cliente.beta.threads.messages.lis(thread_id = thread.id).data)
#             resposta = historico[0]
#             print(historico)
#             return resposta

#         except Exception as erro:
#                 repeticao += 1
#                 if repeticao >= maximo_tentativas:
#                         return "Erro no GPT: %s" % erro
#                 print('Erro de comunicação com OpenAI:', erro)
#                 sleep(1)
