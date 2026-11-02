from src.book_store import BookStore


def test_add_book_adds_book_to_list():
    store = BookStore()
    store.addBook("Guido van Rossum", "Ormar på ett plan")
    assert len(store.books) == 1