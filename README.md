# qa_python_sprint_4
1. Проверка добавления книги с валидным названием (`test_add_new_book_new_name_3_chars_added`).
2. Проверка добавления книги с невалидными названиями (test_add_new_book_negative_input_not_added`).
3. Проверка установки жанра книги с валидными данными (`test_set_book_genre_positie_input_set`).
4. Проверка установки жанра книги с валидными данными (`test_set_book_genre_unknown_genre_not_set`).
5. Проверка вывода жанра существующей книги (`test_get_book_genre_existing_book_returned`).
6. Проверка вывода жанра несуществующей книги (`test_get_book_genre_not_existing_book_not_returned`).
7. Проверка вывода списка книг с определенным жанром (`test_get_books_with_specific_genre_existing_genre_returned`).
8. Проверка вывода списка книг с несуществующим жанром (`test_get_books_with_specific_genre_not_existing_genre_returned`).
9. Проверка вывода словаря books_genre (`test_get_books_genre_returned`).
10. Проверка вывода списка книг, подходящих детям (`test_get_books_for_children_returned`).
11. Проверка добавления книги в "избранное" с валидным названием (`test_add_book_in_favorites_existing_book_added`).
12. Проверка повторного добавления книги в "избранное" (`test_add_book_in_favorites_duplicated_book_not_added`).
13. Проверка добавления книги в "избранное" с невалидными данными (`test_add_book_in_favorites_not_existing_book_not_added`).
14. Провека удаления ранее добавленной книги из "избранное" (`test_delete_book_from_favorites_existing_book_removed`).
15. Провека удаления несуществующей книги из "избранное" (`test_delete_book_from_favorites_not_existing_book_not_removed`).
16. Проверка вывод списка "избранное" (`test_get_list_of_favorites_books_returned`).