from Arquivos.arquivos import carregar_acervo

from Crud.crud import(
    cadastrar_livro,
    listar_livros,
    buscar_livro,
    editar_livro,
    registrar_venda,
    excluir_livro
)

acervo_livros = carregar_acervo()
isbns_cadastrados = set()

for livro in acervo_livros:
    isbns_cadastrados.add(livro["isbn"])

# Menu principal
def menu_principal():

 Sistema_ativo = True
 print("\n Biblioteca São Pedro")

 if acervo_livros == []:
     print("O acervo está em branco")
 else:
     print("Acervo carregado!")    
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

            editar_livro(acervo_livros,isbns_cadastrados)

        elif opcao == "5":

            registrar_venda(acervo_livros)

        elif opcao == "6":

            excluir_livro(acervo_livros, isbns_cadastrados)

        elif opcao == "7":

            print(acervo_livros)

        elif opcao == "8":

            print("Encerrando o sistema...")
            sistema_ativo = False

        else:

            print("Opção inválida. Tente novamente.")


# Iniciar o sistema
menu_principal()
