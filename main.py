from Arquivos.arquivos import carregar_acervo

acervo_livros = carregar_acervo()
isbns_cadastrados = set()

for livros in acervo_livros:
    isbns_cadastrados.add(livros["isbn"])
from Crud.crud import cadastrar_livro, listar_livros


# Dados do sistema
acervo_livros = []
isbns_cadastrados = set()

arquivo_encontrado = False

generos_aceitos = (
    "romance",
    "ficção",
    "terror",
    "fantasia",
    "historia",
    "outros"
)

estados_aceitos = ("novo", "seminovo", "usado")


print("Sebo de livros")

if arquivo_encontrado == False:
    print("Arquivos não encontrados")
    print("Iniciando com acervo vazio")

elif acervo_livros == []:
    print("O acervo está vazio")

else:
    print("Acervo disponível:")
    print(acervo_livros)


# Requisito 5 - Buscar livro
def buscar_livro(acervo_livros):

    print("\nBUSCAR LIVRO")
    print("1 - Buscar pelo ISBN")
    print("2 - Buscar pelo título")

    opcao_busca = input("Escolha uma opção: ")
    encontrado = False

    if opcao_busca == "1":

        codigo_busca = input("Digite o ISBN: ").strip()

        if codigo_busca == "":
            print("Digite um ISBN válido.")
            return

        for livro in acervo_livros:

            if str(livro["isbn"]).lower() == codigo_busca.lower():
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


# Requisito 6 - Editar livro
def editar_livro(acervo_livros, isbns_cadastrados):

    print("\nEDITAR LIVRO")

    codigo_busca = input(
        "Digite o código do livro: "
    ).strip().lower()

    for livro in acervo_livros:

        if str(livro["codigo"]).lower() == codigo_busca:

            print("\nDados atuais do livro:")

            print("Código:", livro["codigo"])
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("ISBN:", livro["isbn"])
            print("Gênero:", livro["genero"])
            print("Estado:", livro["estado"])
            print("Preço:", livro["preco"])
            print("Quantidade:", livro["quantidade"])

            print("\nAperte Enter para manter o valor atual.")

            # Editar título
            novo_titulo = input("Novo título: ").strip()

            if novo_titulo != "":
                livro["titulo"] = novo_titulo

            # Editar autor
            novo_autor = input("Novo autor: ").strip()

            if novo_autor != "":
                livro["autor"] = novo_autor

            # Editar ISBN
            while True:

                novo_isbn = input("Novo ISBN: ").strip()

                if novo_isbn == "":
                    break

                elif len(novo_isbn) != 13 or not novo_isbn.isdigit():
                    print("O ISBN deve possuir 13 dígitos.")

                elif novo_isbn in isbns_cadastrados and novo_isbn != livro["isbn"]:
                    print("ISBN já cadastrado.")

                else:
                    isbns_cadastrados.discard(livro["isbn"])
                    livro["isbn"] = novo_isbn
                    isbns_cadastrados.add(novo_isbn)
                    break

            # Editar gênero
            print("\nGêneros aceitos:", generos_aceitos)

            while True:

                novo_genero = input("Novo gênero: ").strip().lower()

                if novo_genero == "":
                    break

                elif novo_genero in generos_aceitos:
                    livro["genero"] = novo_genero
                    break

                else:
                    print("Gênero inválido.")

            # Editar estado
            print("\nEstados aceitos:", estados_aceitos)

            while True:

                novo_estado = input("Novo estado: ").strip().lower()

                if novo_estado == "":
                    break

                elif novo_estado in estados_aceitos:
                    livro["estado"] = novo_estado
                    break

                else:
                    print("Estado inválido.")

            # Editar preço
            while True:

                novo_preco = input("Novo preço: ").strip()

                if novo_preco == "":
                    break

                try:
                    novo_preco = float(novo_preco.replace(",", "."))

                    if 0 < novo_preco < float("inf"):
                        livro["preco"] = novo_preco
                        break

                    else:
                        print("O preço deve ser positivo e finito.")

                except ValueError:
                    print("Digite um preço válido.")

            # Editar quantidade
            while True:

                nova_quantidade = input("Nova quantidade: ").strip()

                if nova_quantidade == "":
                    break

                try:
                    nova_quantidade = int(nova_quantidade)

                    if nova_quantidade >= 0:
                        livro["quantidade"] = nova_quantidade
                        break

                    else:
                        print("A quantidade não pode ser negativa.")

                except ValueError:
                    print("Digite uma quantidade válida.")

            print("\nLivro atualizado com sucesso!")
            return

    print("Livro não encontrado.")


# Menu principal
def menu_principal():

 Sistema_ativo = True

 while sistema_ativo:

        print("\n===== SEBO DE LIVROS =====")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livros")
        print("4 - Editar livros")
        print("5 - Registrar vendas")
        print("6 - Excluir livros")
        print("7 - Relatórios")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":

            cadastrar_livro(acervo_livros, isbns_cadastrados)

        elif opcao == "2":

            listar_livros(acervo_livros)

        elif opcao == "3":

            buscar_livro(acervo_livros)

        elif opcao == "4":

            editar_livro(acervo_livros)

        elif opcao == "5":

            print(acervo_livros)

        elif opcao == "6":

            print(acervo_livros, isbns_cadastrados)

        elif opcao == "7":

            print(acervo_livros)

        elif opcao == "8":

            print("Encerrando o sistema...")
            sistema_ativo = False

        else:

            print("Opção inválida. Tente novamente.")


# Iniciar o sistema
menu_principal()
