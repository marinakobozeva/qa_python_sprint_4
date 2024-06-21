import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_books_genre_is_empty_true(self, books_collector):
        assert len(books_collector.books_genre) == 0

    def test_favorites_is_empty_true(self, books_collector):
        assert len(books_collector.favorites) == 0

    def test_genre_is_not_empty_true(self, books_collector):
        assert len(books_collector.genre) != 0

    def test_genre_age_rating_is_not_empty_true(self, books_collector):
        assert len(books_collector.genre_age_rating) != 0

    def test_add_new_book_new_name_3_chars_added(self, books_collector):
        name = "abc"
        books_collector.add_new_book(name)
        assert name in books_collector.books_genre

    @pytest.mark.parametrize('name', ["а" * 41, ""])
    def test_add_new_book_negative_input_not_added(self, books_collector, name):
        books_collector.add_new_book(name)
        assert name not in books_collector.books_genre

    def test_set_book_genre_positive_input_set(self, books_collector):
        name = "abc"
        genre = "Фантастика"
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == genre

    def test_set_book_genre_unknown_genre_not_set(self, books_collector):
        name = "cat"
        genre = "Антиутопия"
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == ""

    def test_get_book_genre_existing_book_returned(self, books_collector):
        name = "abc"
        genre = "Фантастика"
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_book_genre(name)

    def test_get_book_genre_not_existing_book_not_returned(self, books_collector):
        name = "test"
        assert books_collector.get_book_genre(name) is None

    def test_get_books_with_specific_genre_existing_genre_returned(self, books_collector_filled):
        genre = "Фантастика"
        expected_result = ["abc", "fantasy"]
        assert expected_result == books_collector_filled.get_books_with_specific_genre(genre)

    def test_get_books_with_specific_genre_not_existing_genre_not_returned(self, books_collector_filled):
        genre = "Романтика"
        expected_result = []
        assert expected_result == books_collector_filled.get_books_with_specific_genre(genre)

    def test_get_books_genre_returned(self, books_collector_filled):
        expected_result = {
            "abc": "Фантастика",
            "love": "",
            "cat": "",
            "fantasy": "Фантастика",
        }
        assert expected_result == books_collector_filled.get_books_genre()

    def test_get_books_for_children_returned(self, books_collector_filled):
        expected_result = ["abc", "fantasy"]
        assert expected_result == books_collector_filled.get_books_for_children()

    def test_add_book_in_favorites_existing_book_added(self, books_collector_filled):
        name = "abc"
        books_collector_filled.add_book_in_favorites(name)
        assert name in books_collector_filled.favorites

    def test_add_book_in_favorites_duplicated_book_not_added(self, books_collector_filled):
        name = "abc"
        books_collector_filled.add_book_in_favorites(name)
        fav_length = len(books_collector_filled.favorites)
        books_collector_filled.add_book_in_favorites(name)
        assert fav_length == len(books_collector_filled.favorites)

    def test_add_book_in_favorites_not_existing_book_not_added(self, books_collector_filled):
        name = "python"
        books_collector_filled.add_book_in_favorites(name)
        assert name not in books_collector_filled.favorites

    def test_delete_book_from_favorites_existing_book_removed(self, books_collector_filled):
        name = "abc"
        books_collector_filled.add_book_in_favorites(name)
        books_collector_filled.delete_book_from_favorites(name)
        assert name not in books_collector_filled.favorites

    def test_delete_book_from_favorites_not_existing_book_not_removed(self, books_collector_filled):
        name = "python"
        books_collector_filled.delete_book_from_favorites(name)
        assert name not in books_collector_filled.favorites

    def test_get_list_of_favorites_books_returned(self, books_collector_filled):
        books_collector_filled.add_book_in_favorites("fantasy")
        assert books_collector_filled.get_list_of_favorites_books() == ["fantasy"]

