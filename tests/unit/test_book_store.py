from src.book_store import BookStore


def test_add_book_adds_book_to_list():
    store = BookStore()
    store.addBook("Guido van Rossum", "Ormar på ett plan")
    assert len(store.books) == 1


def test_add_book_gives_each_book_its_own_id():
    store = BookStore()
    store.addBook("Guido van Rossum", "Ormar på ett plan")
    store.addBook("Linus Torvalds", "Git Blame and Other Ways to Lose Friends")
    assert store.books[0]["id"] == 1
    assert store.books[1]["id"] == 2


def test_toggle_favorite_marks_book_as_favorite():
    store = BookStore()
    store.addBook("Guido van Rossum", "Ormar på ett plan")
    store.toggleFavorite(1)
    assert store.books[0]["fav"] is True