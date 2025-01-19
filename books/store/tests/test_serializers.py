# Проводим тестирование наших сериализаторов

# default django
from unittest import TestCase

# my_project
from store.serializers import BookSerializer
from store.models import Book


class BookSerializerTestCase(TestCase):
    def test_ok(self):

        book_1 = Book.objects.create(name="Test book 1", price="25")
        book_2 = Book.objects.create(name="Test book 2", price="30")

        data = BookSerializer([book_1, book_2], many=True).data

        expected_data = [
            # "price": "25.00" потому что в модели ето DecimalField
            {"id": book_1.id, "name": "Test book 1", "price": "25.00"},
            {"id": book_2.id, "name": "Test book 2", "price": "30.00"},
        ]

        self.assertEqual(expected_data, data)
