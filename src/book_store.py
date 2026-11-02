class BookStore:
    def __init__(self):
        self.books = []

    def addBook(self, author, title):
        self.books.append({"author": author, "title": title})