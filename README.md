# Sprint_4

## Фикстуры conftest.py
    collector - создается пустой класс collector
    collector_with_books_and_genres - словарь books_genre заполняется данными
    favorites - список favorites заполняется данными

## Метод add_new_book
### test_add_new_book_add_same_book_three_times_book_added_once
    Проверяет добавление одной книги три раза подряд. 
    Метод позволяет добавить книгу только один раз. После этого длина словаря остается неизменной. 

###  test_add_new_book_more_than_40_symbols_in_book_name_books_not_added  
    Параметрический тест, проверяющий невозможность добавить в словарь книги с количеством символов
    больше 40 в названии. Диапазон количества символов от 41 до + беск. Параметр symbols в самой функции
    не используется. При выводе pytest он показывает сколько символов в каждом названии книги.

## Метод set_book_genre
### test_set_book_genre_set_genre_from_genre_list_genre_set
    Проверяет успешное добавление жанра из списка genre для киги существующей в списке books_genre. 

### test_set_book_genre_set_genre_not_from_genre_list_genre_not_set
    Проверяет невозможность добавить книге жанр не из списка genre.

## Метод get_book_genre
### test_get_book_genre_for_book_from_books_genre_shows_book_genre
    Проверяет успешный вывод жанра для книги, существующей в books_genre.

## Метод get_books_with_specific_genre
### test_get_books_with_specific_genre_for_books_from_books_genre_shows_two_books
    Проверяет корректный вывод книг для заданного жанра. В изначальном словаре есть две книги жанра 'Ужасы'.
    Метод успешно выводит список из этих книг.

### test_get_books_with_specific_genre_book_genre_not_from_genre_list_shows_none
    Проверяет невозможность вывода книг с несуществующим жанром. Жанра 'Боевик' нет в списке genre.
    Метод возвращает пустой список.

## Метод get_books_genre
### test_get_books_genre_shows_list_of_books_with_genres
    Проверяет успешный вывод словаря books_genre и сравнивает его с эталонным.

## Метод get_books_for_children
### test_get_books_for_children_shows_books_with_no_age_rating
    Проверяет успешный выбор и вывод из books_genre только книг не имеющих возрастного рейтинга.  
    Вывод метода сравнивается с эталонным.

## Метод add_book_in_favorites
### test_add_book_in_favorites_book_from_books_genre_book_added
    Проверяет успешное добавление в список favorites книги, существующей в словаре books_genre.

### test_add_book_in_favorites_book_not_from_books_genre_book_not_added
    Проверяет невозможность добавить в список favorites книги не из словаря books_genre.

###  test_add_book_in_favorites_add_same_book_three_times_book_added_once
    Проверяет добавление в favorites одной книги три раза подряд. 
    Метод позволяет добавить книгу только один раз. После этого длина списка остается неизменной.

## Метод delete_book_from_favorites
### test_delete_book_from_favorites_delete_one_book_book_deleted
    Проверяет успешное удаление ранее добавленной книги из favorites.

## Метод get_list_of_favorites_books
### test_get_list_of_favorites_books_shows_list_of_favorite_books
    Проверяет успешный вывод списка favorites и сравнивает его с эталонным.