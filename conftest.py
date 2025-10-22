import pytest
from main import BooksCollector

#создается пустой класс collector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

