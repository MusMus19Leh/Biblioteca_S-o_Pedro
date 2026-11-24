
from Crud.crud import cadastrar_livro, listar_livros
acervo_livros = []
isbns_cadastrados = set()
quantidade_livros = 0
arquivo_encontrado = False 

generos_aceitos = ("romance,"ficção","terror", "fantasia", "historia", "outos")

estados_aceitos = ("novo","seminovo", "usado")


print("Sebo de livros")

if arquivo_encontrado == False:
    print("Arquivos não encontrados")
    print("Iniciando com acervo vazio")

elif acervo_livros == []:
    print("O acervo está vazio")

else:
    print("Acervo que está disponível:")
    print(acervo_livros)


    print("Acervo que está disponivel:")
    print(acervo_livros)

def menu_principal ():

Sistema_ativo = True
while Sistema_ativo:

        print("\nSebo de livros opções")
        print("1-Cadastrar livro")
        print("2-Listar livros")
        print("3-Buscar livros")
        print("4-Editar livros")
        print("5-Registrar vendas")
        print("6-Excluir livros")
        print("7-Relatórios")
        print("8-Sair"
        
    opçao= input("Escolher uma opção:")
    
        

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

    print("BUSCAR LIVRO ")
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


# Iniciar o sistema
menu_principal()
        print("opção invalida.")

    def buscar_livro(acervo_livros)

    print("Buscar livros")
    print("1- Buscar pelo ISBN")
    print("2- Buscar pelo titulo")

opcao_buscar = input("Escolher uma opcao")
encontrado = false 
if opcão_buscar == "1":

    codigo_buscar = input("Digite o ISBN:").strip().lower()
    if codigo_buscar == "":
        print("Digite um ISBN valido.")

    for livros in acervo_livros:
        if str(livros["isbn"].lower() == codigo_busca:
            print("Livro encontado:")
            print (livro)
            encontado = true
elif opcao_buscar == "2":

    titulos_buscar = input("Digite o titulo ou parte dele:").strip().lower()
    if titulo_buscar ==:
        print("Digite um titulo valido.")
        return

for livro in acervo_livros:

    if titulos_busca in livro["titulos"]
        print("Livros encontado:")
        print(livro)
        encontado = true

else:
    print("Opção de busca invalido")
    return

if encontado == false:
    print("nehum livro encontado")

    


def editar_livro(acervo_livros, isbns_cadastrados):

    print("Editar livro")

    codigo_busca = input("Digite o código do livro: ").strip().lower()

    for livro in acervo_livros:

        if str(livro["codigo"]).lower() == codigo_busca:

            print("Dados atuais do livro:")

            print("Código:", livro["codigo"])
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("ISBN:", livro["isbn"])
            print("Gênero:", livro["genero"])
            print("Estado:", livro["estado"])
            print("Preço:", livro["preco"])
            print("Quantidade:", livro["quantidade"])

            print("Aperte Enter para manter o valor atual.")

            
            novo_titulo = input("Novo título: ").strip()

            if novo_titulo != "":
                livro["titulo"] = novo_titulo

            
            novo_autor = input("Novo autor: ").strip()

            if novo_autor != "":
                livro["autor"] = novo_autor

            
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

            
            print("Gêneros aceitos:", generos_aceitos)

            while True:

                novo_genero = input("Novo gênero: ").strip()

                if novo_genero == "":
                    break

                elif novo_genero in generos_aceitos:
                    livro["genero"] = novo_genero
                    break

                else:
                    print("Gênero inválido.")

            
            print("Estados aceitos:", estados_aceitos)

            while True:

                novo_estado = input("Novo estado: ").strip()

                if novo_estado == "":
                    break

                elif novo_estado in estados_aceitos:
                    livro["estado"] = novo_estado
                    break

                else:
                    print("Estado inválido.")

            
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

            print("Livro atualizado com sucesso!")
            return

    print("Livro não encontrado.")





 



    

        
