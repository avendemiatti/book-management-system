# main.py
from service.category_service import CategoryService
from service.author_service import AuthorService
from service.editor_service import EditorService
from service.book_service import BookService

# Import the new menu modules
from menu.category_menu import run_category_menu
from menu.author_menu import run_author_menu
from menu.editor_menu import run_editor_menu
from menu.book_menu import run_book_menu

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
            run_category_menu(category_service)
        elif escolha_main == '2':
            run_editor_menu(editor_service)
        elif escolha_main == '3':
            run_author_menu(author_service)
        elif escolha_main == '4':
            run_book_menu(book_service)
        elif escolha_main == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
