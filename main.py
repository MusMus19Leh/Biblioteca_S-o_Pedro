from Crud.crud import cadastrar_livro, listar_livros
acervo_livros = []
isbns_cadastrados = set()
quantidade_livros = 0
arquivo_encontrado = False 

generos_aceitos = ("romance,"ficção","terror", "fantasia", "historia", "outos")



print ("Sebo de livros")


if arquivo_encontrado == False:
    print("Arquivos não encontrados")
    print("Iniciando com acervo vazio")

elif acervo_livros == []:
    print("O acervo está vazio")

else:
    print("Acervo que está disponivel:")
    print(acervo_livros)

def menu_principal ():

Sistema_ativo = True
while Sistema_ativo:

    print("Sebo de livros opções")
    print("1-Cadastrar livro")
    print("2-Listar livros")
    print("3-Buscar livros")
    print("4-Editatr livros")
    print("5-Registrar vendas")
    print("6-Excluir livros")
    print("7-Relatorios")
    print("8-Sair")

    opçao= input("Escolher uma opção:")
    if opçao == "1":
        cadastrar_livro(acervo_livros, isbns_cadastrados)

    elif opçao == "2":
        listar_livros(acervo_livros)
    
    elif opçao == "3":
        buscar_livro(acervo_livros)

    elif opçao == "4":
        print("opção Editar livro selecionados")

    elif opçao == "5":
        print("opção Registrar livro vendido ")

    elif opçao == "6":
        print("Opçao excluir livro selecionado")

    elif opçao == "7":
        print("opção mostrar relatorio")

    elif opçao == "8":
        break 
    else:
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

    

        
    
