import pytest

@pytest.fixture()
def clear_books_database() -> None:
    print("[FIXTURE] Удаляем все книги из базы данных")

@pytest.fixture()
def fill_books_database() -> None:
    print("[FIXTURE] Заполняем книги в базы данных")

@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books():
    print("reading")

@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    def test_read_book(self):
        print("reading")

    def test_delete_book(self):
        print("delete")


