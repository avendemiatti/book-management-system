# model/category.py

class Category:

    def __init__(self, category_id, name):

        self.category_id = category_id  # "self" refers to the instance being created
        self.name = name

    def __str__(self):

        return f"Category[ID={self.category_id}, Name={self.name}]"
