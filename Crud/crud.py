def cadastrar_livros(acervo_livros, isbns_cadastros):
    """ livros novos para serem cadastro no acervo, que 
    recebe uma lista de livros com catalogo e o ISBNs já inseridos
    """

print("\n Cadastro de livros")

while True:
    titulo = input("Digite o título do livro:")

    if titulo != " ":
        break
    else:
        print("Está vázio. Por favor,preencha novamente seu título!")  

while True:
    autor = input("Digite o nome do autor:")

    if autor != " ":         
        break
    else:
        print("Está vázio. Por favor,preencha novamente o nome do autor!")  

while True:
    isbn = input("Digite o ISBN do livro:")

    if not isbn.isdigit():
       print("Erro: Apenas números!")
    
    elif len(isbn) != 13:
       print("Erro: ISBN deve conter 13 dígitos em seu código de barra ")

    elif isbn in isbns_cadastrados:
       print("Erro: este ISBN já está cadastrado.")

    else:
       break         