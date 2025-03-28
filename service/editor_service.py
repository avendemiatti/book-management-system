# service/editor_service.py

from dao.editor_dao import EditorDAO
from model.editor import Editor

class EditorService:
    """
    Manages business logic for Editors.
    """

    def __init__(self):
        self.editor_dao = EditorDAO()

    def list_editors(self):
        """
        Retrieve all editors.
        :return: List of Editor objects.
        """
        return self.editor_dao.list_all()

    def add_editor(self, editor_id, name, address, phone):
        """
        Create and store a new Editor. 
        :param editor_id: Unique identifier.
        :param name: Name of the editor (e.g. "Springer", "Penguin Books").
        :param address: Address details (optional).
        :param phone: Contact phone number.
        """
        new_editor = Editor(editor_id, name, address, phone)
        self.editor_dao.create(new_editor)

    def delete_editor(self, editor_id):
        """
        Remove an Editor by ID.
        :param editor_id: The ID of the editor to remove.
        """
        self.editor_dao.delete(editor_id)

    def get_editor_by_id(self, editor_id):
        """
        Find an Editor by its unique ID.
        :param editor_id: The ID to look up.
        :return: Editor object if found, otherwise None.
        """
        return self.editor_dao.find_by_id(editor_id)
