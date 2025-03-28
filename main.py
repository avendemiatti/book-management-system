# main.py

from service.category_service import CategoryService
from service.author_service import AuthorService
from service.editor_service import EditorService
from service.book_service import BookService

def main():
    category_service = CategoryService()
    author_service = AuthorService()
    editor_service = EditorService()
    book_service = BookService()

    while True:
        print('[Menu Principal] Escolha uma das seguintes opções:')
        print('1 - Categorias')
        print('2 - Editoras')
        print('3 - Autores')
        print('4 - Livros')
        print('0 - Sair do programa')
        escolha_main = input('Digite a opção: ')

        if escolha_main == '1':
            while True:
                print('\n[Categoria] Escolha uma das seguintes opções:')
                print('1 - Listar todas as categorias')
                print('2 - Adicionar nova categoria')
                print('3 - Excluir categoria')
                print('4 - Ver categoria por ID')
                print('0 - Voltar ao menu anterior')
                escolha = input('Digite a opção: ')

                if escolha == '1':
                    # List all categories
                    categories = category_service.list_categories()
                    if categories:
                        print("\n=== Todas as Categorias ===")
                        for cat in categories:
                            print(cat)
                    else:
                        print("\nNenhuma categoria encontrada.")
                
                elif escolha == '2':
                    # Add a new category
                    name = input("Digite o nome da categoria: ")
                    category_service.add_category(name)
                    print(f"A nova categoria '{name}' foi adicionada com sucesso!")
   
                elif escolha == '3':
                    # Delete a category by ID
                    cat_id = input("Digite o ID da categoria que deseja excluir: ")
                    category_service.delete_category(cat_id)
                    print("Categoria excluída com sucesso (se existia).")
                
                elif escolha == '4':
                    # Get category by ID
                    cat_id = input("Digite o ID da categoria: ")
                    category = category_service.get_category_by_id(cat_id)
                    if category:
                        print(f"Categoria encontrada: {category}")
                    else:
                        print("Categoria não encontrada.")
                
                elif escolha == '0':
                    # Exit the Category menu
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha_main == '2':
            while True:
                print('\n[Editoras] Escolha uma das seguintes opções:')
                print('1 - Listar todas as editoras')
                print('2 - Adicionar nova editora')
                print('3 - Excluir editora')
                print('4 - Ver editora por ID')
                print('0 - Voltar ao menu anterior')
                escolha = input('Digite a opção: ')

                if escolha == '1':
                    # List all editors
                    editors = editor_service.list_editors()
                    if editors:
                        print("\n=== Todas as Editoras ===")
                        for editor in editors:
                            print(editor)
                    else:
                        print("\nNenhuma editora encontrada.")

                elif escolha == '2':
                    # Add a new editor
                    editor_id = input("Digite o ID da editora: ")
                    name = input("Digite o nome da editora: ")
                    address = input("Digite o endereço da editora: ")
                    phone = input("Digite o telefone da editora: ")
                    editor_service.add_editor(editor_id, name, address, phone)
                    print("Editora adicionada com sucesso!")

                elif escolha == '3':
                    # Delete an editor by ID
                    editor_id = input("Digite o ID da editora que deseja excluir: ")
                    editor_service.delete_editor(editor_id)
                    print("Editora excluída com sucesso (se existia).")

                elif escolha == '4':
                    # Get editor by ID
                    editor_id = input("Digite o ID da editora: ")
                    editor = editor_service.get_editor_by_id(editor_id)
                    if editor:
                        print(f"Editora encontrada: {editor}")
                    else:
                        print("Editora não encontrada.")

                elif escolha == '0':
                    # Exit the Editor menu
                    break

                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha_main == '3':
            while True:
                print('\n[Autores] Escolha uma das seguintes opções:')
                print('1 - Listar todos os autores')
                print('2 - Adicionar novo autor')
                print('3 - Excluir autor')
                print('4 - Ver autor por ID')
                print('0 - Voltar ao menu anterior')
                escolha = input('Digite a opção: ')

                if escolha == '1':
                    # List all authors
                    authors = author_service.list_authors()
                    if authors:
                        print("\n=== Todos os Autores ===")
                        for author in authors:
                            print(author)
                    else:
                        print("\nNenhum autor encontrado.")

                elif escolha == '2':
                    # Add a new author
                    author_id = input("Digite o ID do autor: ")
                    name = input("Digite o nome do autor: ")
                    email = input("Digite o email do autor: ")
                    phone = input("Digite o telefone do autor: ")
                    bio = input("Digite a biografia do autor: ")
                    author_service.add_author(author_id, name, email, phone, bio)
                    print("Autor adicionado com sucesso!")

                elif escolha == '3':
                    # Delete an author by ID
                    author_id = input("Digite o ID do autor que deseja excluir: ")
                    author_service.delete_author(author_id)
                    print("Autor excluído com sucesso (se existia).")

                elif escolha == '4':
                    # Get author by ID
                    author_id = input("Digite o ID do autor: ")
                    author = author_service.get_author_by_id(author_id)
                    if author:
                        print(f"Autor encontrado: {author}")
                    else:
                        print("Autor não encontrado.")

                elif escolha == '0':
                    # Exit the Author menu
                    break

                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha_main == '4':
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
                    book_id = input("Digite o ID do livro: ")
                    title = input("Digite o título do livro: ")
                    summary = input("Digite o resumo do livro: ")
                    year = input("Digite o ano de publicação: ")
                    pages = input("Digite o número de páginas: ")
                    isbn = input("Digite o ISBN do livro: ")
                    category_id = input("Digite o ID da categoria: ")
                    editor_id = input("Digite o ID da editora: ")
                    author_id = input("Digite o ID do autor: ")
                    book_service.add_book(book_id, title, summary, year, pages, isbn, category_id, editor_id, author_id)
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
                    
        elif escolha_main == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
