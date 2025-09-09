def ver_livros_disponiveis(lista_livros):
    if not lista_livros:
        print("Nenhum livro disponível no momento.\n")
        return

    print("--------------------------------------------------")
    print("LIVROS DISPONÍVEIS PARA LEITURA")
    for livro in lista_livros:
        print(f"{livro['id']} - {livro['titulo']} ({livro['ano']}) - Autor: {livro['autor']} - Gênero: {livro['genero']}")
    print("--------------------------------------------------\n")
