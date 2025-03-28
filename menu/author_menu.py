def run_author_menu(author_service):
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
            name = input("Digite o nome do autor: ")
            email = input("Digite o email do autor: ")
            phone = input("Digite o telefone do autor: ")
            bio = input("Digite a biografia do autor: ")
            author_service.add_author(name, email, phone, bio)
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
