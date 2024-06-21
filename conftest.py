import pytest
from main import BooksCollector


@pytest.fixture
def books_collector():
    return BooksCollector()

@pytest.fixture
def books_collector_filled():
    bc = BooksCollector()
    info = [
        ("abc", "Фантастика"),
        ("love", "Романтика"),
        ("cat", ""),
        ("fantasy", "Фантастика"),
    ]

    for name, genre in info:
        bc.add_new_book(name)
        if genre != "":
            bc.set_book_genre(name, genre)
    return bc

