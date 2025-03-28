class Book:
    def __init__(
        self, 
        book_id, 
        title, 
        summary, 
        year, 
        pages, 
        isbn, 
        category_id, 
        editor_id, 
        author_id
    ):
        self.book_id = book_id
        self.title = title
        self.summary = summary
        self.year = year
        self.pages = pages
        self.isbn = isbn
        self.category_id = category_id
        self.editor_id = editor_id
        self.author_id = author_id

    def __str__(self):
        return (f"Book[ID={self.book_id}, Title={self.title}, Summary={self.summary}, "
                f"Year={self.year}, Pages={self.pages}, ISBN={self.isbn}, "
                f"Category ID={self.category_id}, Editor ID={self.editor_id}, "
                f"Author ID={self.author_id}]")