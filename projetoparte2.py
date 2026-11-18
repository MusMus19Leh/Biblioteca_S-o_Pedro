opçao = ""
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
        print("Opção cadastrar livros selecionados")

    elif opçao == "2":
        print("Opção listar filmes selecionados ")
    
    elif opçao == "3":
        print("Opção buscar filmes selecionados")

    elif opçao == "4":
        print("opção Editar filmes selecionados")

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
        
    

