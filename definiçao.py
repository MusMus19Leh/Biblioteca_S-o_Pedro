


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



menu_principal()

 


