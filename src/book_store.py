class BookStore:
    def __init__(self):
        self.books = []

    def addBook(self, author, title):
        book_id = len(self.books) + 1
        self.books.append({"id": book_id, "author": author, "title": title, "fav": False})

    def toggleFavorite(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                book["fav"] = not book["fav"]