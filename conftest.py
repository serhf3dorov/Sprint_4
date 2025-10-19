import pytest
from main import BooksCollector

#создается пустой класс collector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

#словарь books_genre заполняется данными
@pytest.fixture
def collector_with_books_and_genres(collector):
    books = {'Солярис': 'Фантастика', 'Оно': 'Ужасы', 'Пуаро': 'Детективы', 'Моана': 'Мультфильмы', 'Ревизор': 'Комедии', 'Пятачок в угаре': 'Ужасы'}
    for book, genre in books.items():
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
    return collector_with_books_and_genres

#список favorites заполняется данными
@pytest.fixture
def favorites(collector, collector_with_books_and_genres):
    for book in collector.books_genre.keys():
        collector.add_book_in_favorites(book)
    return favorites

