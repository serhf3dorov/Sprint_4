from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # add_new_book
    def test_add_new_book_add_same_book_three_times_book_added_once(self, collector):
        collector.add_new_book('Солярис')
        collector.add_new_book('Солярис')
        collector.add_new_book('Солярис')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book, symbols',
        [['Что делать, если ваш кот хочет вас убить!', 41],
        ['Что делать,, если ваш кот хочет вас убить!', 42],
        ['Что делать, если ваш кот хочет вас убить и съесть на ужин', 57]])
    def test_add_new_book_more_than_40_symbols_in_book_name_books_not_added(self, book, symbols, collector):
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 0

    # set_book_genre
    def test_set_book_genre_set_genre_from_genre_list_genre_set(self, collector):
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        assert collector.get_books_genre().get('Солярис') == 'Фантастика'

    def test_set_book_genre_set_genre_not_from_genre_list_genre_not_set(self, collector):
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Боевик')
        assert collector.get_books_genre().get('Солярис') == ''

    # get_book_genre
    def test_get_book_genre_for_book_from_books_genre_shows_book_genre(self, collector, collector_with_books_and_genres):
        assert collector.get_book_genre('Солярис') == 'Фантастика'

    # get_books_with_specific_genre
    def test_get_books_with_specific_genre_for_books_from_books_genre_shows_two_books(self, collector, collector_with_books_and_genres):
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно', 'Пятачок в угаре']

    def test_get_books_with_specific_genre_book_genre_not_from_genre_list_shows_none(self, collector, collector_with_books_and_genres):
        assert collector.get_books_with_specific_genre('Боевик') == []

    # get_books_genre
    def test_get_books_genre_shows_list_of_books_with_genres(self, collector, collector_with_books_and_genres):
        books = {'Солярис': 'Фантастика', 'Оно': 'Ужасы', 'Пуаро': 'Детективы', 'Моана': 'Мультфильмы', 'Ревизор': 'Комедии', 'Пятачок в угаре': 'Ужасы'}
        assert collector.get_books_genre() == books

    # get_books_for_children
    def test_get_books_for_children_shows_books_with_no_age_rating(self, collector, collector_with_books_and_genres):
        books_for_children = ['Солярис', 'Моана', 'Ревизор']
        assert collector.get_books_for_children() == books_for_children

    # add_book_in_favorites
    def test_add_book_in_favorites_book_from_books_genre_book_added(self, collector, collector_with_books_and_genres):
        collector.add_book_in_favorites('Солярис')
        assert collector.get_list_of_favorites_books() == ['Солярис']

    def test_add_book_in_favorites_book_not_from_books_genre_book_not_added(self, collector, collector_with_books_and_genres):
        collector.add_book_in_favorites('Капитан Немо')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_add_same_book_three_times_book_added_once(self, collector, collector_with_books_and_genres):
        collector.add_book_in_favorites('Солярис')
        collector.add_book_in_favorites('Солярис')
        collector.add_book_in_favorites('Солярис')
        assert len(collector.get_list_of_favorites_books()) == 1

    # delete_book_from_favorites
    def test_delete_book_from_favorites_delete_one_book_book_deleted(self, favorites, collector, collector_with_books_and_genres):
        collector.delete_book_from_favorites('Солярис')
        assert 'Солярис' not in collector.get_list_of_favorites_books()

    # get_list_of_favorites_books
    def test_get_list_of_favorites_books_shows_list_of_favorite_books(self, favorites, collector, collector_with_books_and_genres):
        favorites =['Солярис','Оно', 'Пуаро', 'Моана', 'Ревизор', 'Пятачок в угаре']
        assert collector.get_list_of_favorites_books() == favorites
