import pytest
from main import BooksCollector


@pytest.fixture(scope='session')
def books_collector():
    return BooksCollector()


def test_add_new_book_new_name_3_chars_added(books_collector):
    name = "abc"
    books_collector.add_new_book(name)
    assert name in books_collector.books_genre

@pytest.mark.parametrize('name', ["а" * 41, ""])
def test_add_new_book_negative_input_not_added(books_collector, name):
    books_collector.add_new_book(name)
    assert name not in books_collector.books_genre


def test_set_book_genre_positie_input_set(books_collector):
    name = "abc"
    genre = "Фантастика"
    books_collector.set_book_genre(name, genre)
    assert books_collector.books_genre[name] == genre

def test_set_book_genre_unknown_genre_not_set(books_collector):
    name = "cat"
    genre = "Антиутопия"
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    assert books_collector.books_genre[name] == ""

def test_get_book_genre_existing_book_returned(books_collector):
    name = "abc"
    assert books_collector.get_book_genre(name)

def test_get_book_genre_not_existing_book_not_returned(books_collector):
    name = "test"
    assert books_collector.get_book_genre(name) is None

def test_get_books_with_specific_genre_existing_genre_returned(books_collector):
    name = "fantasy"
    genre = "Фантастика"
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    expected_result = ["abc", "fantasy"]
    assert expected_result == books_collector.get_books_with_specific_genre(genre)

def test_get_books_with_specific_genre_not_existing_genre_not_returned(books_collector):
    genre = "Романтика"
    expected_result = []
    assert expected_result == books_collector.get_books_with_specific_genre(genre)

def test_get_books_genre_returned(books_collector):
    expected_result = {
        "abc" : "Фантастика",
        "cat" : "",
        "fantasy" : "Фантастика",
    }
    assert expected_result == books_collector.get_books_genre()

def test_get_books_for_children_returned(books_collector):
    expected_result = ["abc", "fantasy"]
    assert expected_result == books_collector.get_books_for_children()

def test_add_book_in_favorites_existing_book_added(books_collector):
    name = "abc"
    books_collector.add_book_in_favorites(name)
    assert name in books_collector.favorites

def test_add_book_in_favorites_duplicated_book_not_added(books_collector):
    name = "abc"
    fav_length = len(books_collector.favorites)
    books_collector.add_book_in_favorites(name)
    assert fav_length == len(books_collector.favorites)

def test_add_book_in_favorites_not_existing_book_not_added(books_collector):
    name = "python"
    books_collector.add_book_in_favorites(name)
    assert name not in books_collector.favorites

def test_delete_book_from_favorites_existing_book_removed(books_collector):
    name = "abc"
    books_collector.delete_book_from_favorites(name)
    assert name not in books_collector.favorites

def test_delete_book_from_favorites_not_existing_book_not_removed(books_collector):
    name = "python"
    books_collector.delete_book_from_favorites(name)
    assert name not in books_collector.favorites

def test_get_list_of_favorites_books_returned(books_collector):
    books_collector.add_book_in_favorites("fantasy")
    assert books_collector.get_list_of_favorites_books() == ["fantasy"]

