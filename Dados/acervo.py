import json 
import os 

caminho_arquivo = os.path.join(
    os.path.dirname(__file__),
    "acervo.json"
)

def carregar_acervo():
    if not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado. Iniciado com acervo vazio")
        return []
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            acervo_livros = json.load(arquivo)

        return acervo_livros

    except (json.JSONDecodeError, OSError):
        print("Não foi possível carregar o arquivo.")
        return []

def salvar_acervo(acervo_livros):

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(
            acervo_livros,
            arquivo,
            ensure_ascii=False,
            indent=4
        )
