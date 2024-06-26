from flask import request, jsonify
from app.services.chatbot_service import bot

class ChatbotController:    
    # def chat(self):
    #     prompt = request.json["msg"]
    #     idade = request.json["age"]
    #     resposta = bot(prompt, idade)
    #     if isinstance(resposta, str):
    #         return resposta 
    #     texto_resposta = resposta.content[0].text.value
    #     return texto_resposta

    def chat(self):
        prompt = request.json["msg"]
        idade = request.json["age"]
        resposta = bot(prompt, idade)
        return jsonify({"response": resposta})
