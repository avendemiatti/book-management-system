class Editor:
    def __init__(self, editor_id, name, address, phone):
        self.editor_id = editor_id
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"Editor[ID={self.editor_id}, Name={self.name}, Endereco={self.address}, Telefone={self.phone}]"