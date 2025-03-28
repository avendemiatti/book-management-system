class Author:
    def __init__(self, author_id, name, email, phone, bio):
        self.author_id = author_id
        self.name = name
        self.email = email
        self.phone = phone
        self.bio = bio

    def __str__(self):
        return f"Author[ID={self.author_id}, Name={self.name}, Email={self.email}, Phone={self.phone}, Bio={self.bio}]"