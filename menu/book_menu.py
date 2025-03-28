def run_book_menu(book_service):
    while True:
        print('\n[Livros] Escolha uma das seguintes opções:')
        print('1 - Listar todos os livros')
        print('2 - Adicionar novo livro')
        print('3 - Excluir livro')
        print('4 - Ver livro por ID')
        print('0 - Voltar ao menu anterior')
        escolha = input('Digite a opção: ')

        if escolha == '1':
            # List all books
            books = book_service.list_books()
            if books:
                print("\n=== Todos os Livros ===")
                for book in books:
                    print(book)
            else:
                print("\nNenhum livro encontrado.")

        elif escolha == '2':
            # Add a new book
            title = input("Digite o título do livro: ")
            summary = input("Digite o resumo do livro: ")
            year = input("Digite o ano de publicação: ")
            pages = input("Digite o número de páginas: ")
            isbn = input("Digite o ISBN do livro: ")
            category_id = input("Digite o ID da categoria: ")
            editor_id = input("Digite o ID da editora: ")
            author_id = input("Digite o ID do autor: ")
            book_service.add_book(title, summary, year, pages, isbn, category_id, editor_id, author_id)
            print("Livro adicionado com sucesso!")

        elif escolha == '3':
            # Delete a book by ID
            book_id = input("Digite o ID do livro que deseja excluir: ")
            book_service.delete_book(book_id)
            print("Livro excluído com sucesso (se existia).")

        elif escolha == '4':
            # Get book by ID
            book_id = input("Digite o ID do livro: ")
            book = book_service.get_book_by_id(book_id)
            if book:
                print(f"Livro encontrado: {book}")
            else:
                print("Livro não encontrado.")

        elif escolha == '0':
            # Exit the Book menu
            break

        else:
            print("Opção inválida. Tente novamente.")