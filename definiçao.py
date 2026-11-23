
def buscar_livro(acervo_livros):

    print(" Buscar livro ")
    print("1 - Buscar pelo ISBN")
    print("2 - Buscar pelo título")

    opcao_busca = input("Escolha uma opção: ")
    encontrado = False

    if opcao_busca == "1":

        codigo_busca = input("Digite o ISBN: ").strip().lower()

        if codigo_busca == "":
            print("Digite um ISBN válido.")
            return

        for livro in acervo_livros:

            if str(livro["isbn"]).lower() == codigo_busca:
                print("Livro encontrado:")
                print(livro)
                encontrado = True

    elif opcao_busca == "2":

        titulo_busca = input(
            "Digite o título ou parte dele: "
        ).strip().lower()

        if titulo_busca == "":
            print("Digite um título válido.")
            return

        for livro in acervo_livros:

            if titulo_busca in livro["titulo"].lower():
                print("Livro encontrado:")
                print(livro)
                encontrado = True

    else:
        print("Opção de busca inválida.")
        return

    if encontrado == False:
        print("Nenhum livro encontrado.")


menu_principal()

