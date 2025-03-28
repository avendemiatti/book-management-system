def run_editor_menu(editor_service):
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
            name = input("Digite o nome da editora: ")
            address = input("Digite o endereço da editora: ")
            phone = input("Digite o telefone da editora: ")
            editor_service.add_editor(name, address, phone)
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