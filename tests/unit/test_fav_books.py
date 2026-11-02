from src.fav_books import FavoriteBooks


def test_add_puts_book_in_favorites():
    favorites = FavoriteBooks()
    book = {"id": 1, "author": "Guido van Rossum", "title": "Ormar på ett plan", "fav": True}
    favorites.add(book)
    assert book in favorites.books

def test_remove_takes_book_out_of_favorites():
    favorites = FavoriteBooks()
    book = {"id": 1, "author": "Guido van Rossum", "title": "Ormar på ett plan", "fav": True}
    favorites.add(book)
    favorites.remove(book)
    assert book not in favorites.books