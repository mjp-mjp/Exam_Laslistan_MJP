from src.book_store import BookStore
from src.fav_books import FavoriteBooks


def test_favorite_book_from_store_ends_up_in_favorites():
    store = BookStore()
    favorites = FavoriteBooks()
    store.addBook("Guido van Rossum", "Ormar på ett plan")
    book = store.books[0]
    store.toggleFavorite(book["id"])
    favorites.add(book)
    assert book["fav"] is True
    assert book in favorites.books