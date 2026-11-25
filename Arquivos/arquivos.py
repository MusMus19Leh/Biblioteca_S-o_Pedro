import json

def carregar_acervo():
    try:
        with open("dados/acervo.jason","r",encoding="urt-8") as arquivo:
            acervo_livros = json.load(arquivo)
        print("Acervo carregadocom sucesso")    
    except FileExistsError:
        acervo_livros = []
        print("Arquivos não encontrados. Iniciando com acervo vazio")
    return acervo_livros       