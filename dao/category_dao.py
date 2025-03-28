class CategoryDAO:
    def __init__(self):
        # Later, we will inject or use the db_connection here
        # For now, maybe keep an in-memory list or just pass
        self.categories = []

    def list_all(self):
        return self.categories

    def create(self, category):
        # Add to the list or eventually write SQL logic
        self.categories.append(category)

    def delete(self, category_id):
        self.categories = [cat for cat in self.categories if cat.category_id != category_id]

    def find_by_id(self, category_id):
        for cat in self.categories:
            if cat.category_id == category_id:
                return cat
        return None
