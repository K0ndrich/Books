# Тестируем Сериализаторы


# django
from django.test import TestCase

# django_rest
from store.serializers import BookSerializer

# my_project
from store.models import Book


class BookSerizalizerTestCase(TestCase):

    def test_ok(self):

        book1 = Book.objects.create(name="Test book 1", price=25)
        book2 = Book.objects.create(name="Test book 2", price=30)

        # data ето данные которые возвращает сериализатор
        data = BookSerializer([book1, book2], many=True).data

        # expected_data ето данные которые мы ожидаем получить от сервера
        # book1.id по названию ячейки (book1) можно обращаться к ее значениям
        expected_data = [
            {"id": book1.id, "name": "Test book 1", "price": "25.00"},
            {"id": book2.id, "name": "Test book 2", "price": "30.00"},
        ]

        self.assertEqual(expected_data, data)
