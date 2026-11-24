def cadastrar_livro(acervo_livros, isbns_cadastrados):
    """ livros novos para serem cadastro no acervo, que 
    recebe uma lista de livros com catalogo e o ISBNs já inseridos
    """

    print("\n Cadastro de livro")

    while True:
        titulo = input("Digite o título do livro:")

        if titulo != "":
            break
        else:
            print("Está vazio. Por favor, preencha novamente seu título!")

    while True:
        autor = input("Digite o nome do autor:")

        if autor != "":
            break
        else:
            print("Está vazio. Por favor, preencha novamente o nome do autor!")

    while True:
        isbn = input("Digite o ISBN do livro: ")

        if not isbn.isdigit():
            print("Erro: o ISBN deve conter apenas números.")

        elif len(isbn) != 13:
            print("Erro: o ISBN deve ter 13 dígitos no código de barras.")

        elif isbn in isbns_cadastrados:
            print("Erro: este ISBN já está cadastrado.")

        else:
            break

def listar_livros(acervo_livros):
    """
    Livros cadastrados no acervo 
    """

    print("\n Acervo de Livros")

    if not acervo_livros:
        print("O acervo está incompleto!")
        return

    print(f"{'código':<10} {'título':<15} {'autor':< 20} {'gênero':< 20} {'preço':<20} {'unidade':<10}")
   
    for livro in acervo_livros:
        titulo = livro["título"]

        if len(titulo) > 25:
            titulo = titulo [:22] +"..."
        
        print(f"{livro['código']:<10} {livro['título']:<15} {livro['autor']:< 20} {livro['gênero']:< 20} R$ {livro['preço']:<20.2f} {livro['unidade']:<10}")

           