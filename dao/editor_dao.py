# dao/editor_dao.py

from model.editor import Editor

class EditorDAO:
    """
    DAO for Editor entities.
    Manages Editor objects in memory before connecting to a real DB.
    """

    def __init__(self):
        """
        Create a list to store Editor objects in memory.
        """
        self.editors = []

    def create(self, editor):
        """
        Add a new Editor object to the list.
        :param editor: An instance of the Editor class.
        """
        self.editors.append(editor)

    def list_all(self):
        """
        Return all Editor objects.
        :return: A list of all editors in memory.
        """
        return self.editors

    def find_by_id(self, editor_id):
        """
        Search for an Editor by ID.
        :param editor_id: The ID of the Editor to find.
        :return: Editor object if found, otherwise None.
        """
        for ed in self.editors:
            if ed.editor_id == editor_id:
                return ed
        return None

    def delete(self, editor_id):
        """
        Remove an Editor by ID.
        :param editor_id: ID of the editor to remove.
        """
        self.editors = [ed for ed in self.editors if ed.editor_id != editor_id]
