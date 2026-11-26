generos_aceitos = [...]
estados_aceitos= [...]

def cadastrar_livro(acervo_livros, isbns_cadastrados):
    """ livros novos para serem cadastro no acervo, que 
    recebe uma lista de livros com catalogo e o ISBNs já inseridos
    """
    
    print("\n Cadastro de livro")
    
    while True:
        titulo = input("Digite o título do livro:")

        if titulo.strip() != "":
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
# Requisitos 4 - Listar_licros
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
   
# Requisito 6 - Editar Livro
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
            print("Estado:", livro["estado"],livro["estado"])
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

                novo_estado = input(f"Novo estado:({livro["estado"]}").strip()

                if novo_estado == "":
                    break

                elif novo_estado in estados_aceitos:
                    livro["estado"]= novo_estado
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

 #requisito 7- Registar vendas
def registrar_venda(acervo_livros):
        
        print("Registrar venda")

        codigo_buscar = input("Digite o codigo do livro:")

        for livro in acervo_livros:
        
            if str(livro["codigo"]).lower() == codigo_buscar.lower():
            
                print("livro:",livro["titulo"])
                print("preço", livro["preco"])
                print("estado",livro["estado"])
                print("estoque disponível:", livro["quantidade"])

                if livro["quantidade"] == 0:
                   print("livro sem estoque.")
                return

            while True:
                try:
                   quantidade_vendida = int(input("Digite a quantidade vendidade:"))
                
                   if quantidade_vendida <= 0:
                      print("A quantidade vendida deve ser maior que zero.")

                   elif quantidade_vendida > livro ["quantidade "]:
                        print("Estoque insuficiente.")

                   else:
                    break
                    
                except ValueError:
                    print("Digite uma quantidade válida:")

            valor_total = livro["preço"] * quantidade_vendida

            if livro["estado"].lower() == "regular":
                    valor_total = valor_total * 0.80
                    print("Desonto de 20% aplicado.")

            livro["quantidade"] -= quantidade_vendida

            print ("venda registrada com sucesso!")
            print(f" valor total de venda: {valor_total:.2f}")

            return

print("livro não encontrado.")


#Requisito 8- excluir livros
    
def excluir_livro(acervo_livros,isbn_cadastrados):
        
    print("Excluir livro")
            
    codigo_busca = input("Digite o codigo do livro:").strip().lower()
    for livro in acervo_livros:    
        if str(livro["codigo"]).lower() == codigo_busca:
            print("Livro encontado:", livro["titulo"])

    while True:

        confirmacao = input("Deseja excluir o livro? (S/N):").strip.lower()
        if confirmacao == "S":
                        
           isbn_cadastrados.discard(livro["isbn"])
           acervo_livros.remove(livro)

           print("Livro excluido com sucesso!")
           return

        elif confirmacao == "N":

            print("Exclusão cancelada.")
            return

        else:
            print("Opação invalida.Digite S ou N")

    print("Livro não encontado.")
  