# menu/category_menu.py

def run_category_menu(category_service):
    """
    Handles all console input/output for 'Category' operations.
    This function is called by main.py when the user selects '1 - Categorias'.
    """
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
