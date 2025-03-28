from dao.editor_dao import EditorDAO
from model.editor import Editor

class EditorService:
    """
    Manages business logic for Editors.
    """

    def __init__(self):
        # Instantiate the DAO so we can call its methods
        self.editor_dao = EditorDAO()

    def list_editors(self):
        """
        Retrieve all editors from the DAO.
        :return: List of Editor objects.
        """
        return self.editor_dao.list_all()

    def add_editor(self, name, address, phone):
        """
        Create an Editor object and send it to the DAO to be inserted into the DB.
        :param name: Name of the editor (e.g. "Springer", "Penguin Books").
        :param address: Address details (optional).
        :param phone: Contact phone number.
        :return: The newly created Editor object.
        """
        new_editor = Editor(None, name, address, phone)
        self.editor_dao.create(new_editor)
        return new_editor

    def delete_editor(self, editor_id):
        """
        Call the DAO to delete the editor by ID.
        :param editor_id: The ID of the editor to remove.
        """
        self.editor_dao.delete(editor_id)

    def get_editor_by_id(self, editor_id):
        """
        Retrieve a single editor by ID through the DAO.
        :param editor_id: The ID to look up.
        :return: Editor object if found, otherwise None.
        """
        return self.editor_dao.find_by_id(editor_id)