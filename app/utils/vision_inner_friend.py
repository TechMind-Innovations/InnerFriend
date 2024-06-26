from openai import OpenAI
from dotenv import load_dotenv
import os
from app.utils.helpers import encodar_imagem

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4o"

def analisar_imagem(caminho_imagem):
    prompt = """
        Você é um amigo íntimo do usuário em que ele confia para falar sobre seu dia a dia.
        Provavelmente o usuário enviou uma imagem. Faça uma análise da foto, e assuma que você sabe e
        processou uma imagem com o Vision e a resposta será informada no formato de saída.
    """

    imagem_base64 = encodar_imagem(caminho_imagem)

    resposta = cliente.chat.completions.create(
        model = modelo,
        messages = [
            {
                "role": "user",
                "content": [
                    { "type": "text", "text": prompt },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64, {imagem_base64}",
                        }
                    }
                ]
            }
        ],
        max_tokens = 300,
    )

    return resposta.choices[0].message.content
