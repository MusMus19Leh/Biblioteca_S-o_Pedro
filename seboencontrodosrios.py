
from Crud.crud import cadastrar_livro, listar_livros

acervo_livros = []
isbns_cadastrados = set()
quantidade_livros = 0
arquivo_encontrado = False

print("Sebo de livros")

if arquivo_encontrado == False:
    print("Arquivos não encontrados")
    print("Iniciando com acervo vazio")

elif acervo_livros == []:
    print("O acervo está vazio")

else:
    print("Acervo que está disponível:")
    print(acervo_livros)


# Menu principal
def menu_principal():

    sistema_ativo = True

    while sistema_ativo:

        print("Sebo de livros opções")
        print("1-Cadastrar livro")
        print("2-Listar livros")
        print("3-Buscar livros")
        print("4-Editar livros")
        print("5-Registrar vendas")
        print("6-Excluir livros")
        print("7-Relatórios")
        print("8-Sair")

        opcao = input("Escolher uma opção: ")

        if opcao == "1":
            cadastrar_livro(acervo_livros, isbns_cadastrados)

        elif opcao == "2":
            listar_livros(acervo_livros)

        elif opcao == "3":
            buscar_livro(acervo_livros)

        elif opcao == "4":
            print("Opção editar livro selecionada")

        elif opcao == "5":
            print("Opção registrar livro vendido")

        elif opcao == "6":
            print("Opção excluir livro selecionado")

        elif opcao == "7":
            print("Opção mostrar relatório")

        elif opcao == "8":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.")


# Requisito 5 - Buscar livro
def buscar_livro(acervo_livros):

    print("Buscar livros")
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

