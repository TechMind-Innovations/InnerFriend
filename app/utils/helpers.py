import base64
def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")

def encodar_imagem(caminho_imagem):
    with open(caminho_imagem, "rb") as arquivo_imagem:
        return base64.b64encode(arquivo_imagem.read()).decode('utf-8')
