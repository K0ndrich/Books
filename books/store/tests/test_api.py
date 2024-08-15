# Провдим тестирование API

from rest_framework.test import APITestCase
from django.urls import reverse
from store.models import Book


class BooksApiTestCase(APITestCase):
    # проверяем GET запрос для нашего api
    def test_get(self):

        book1 = Book.objects.create(name="Test book 1 ", price=25)
        book2 = Book.objects.create(name="Test book 2 ", price=30)
        # reverse(basename_from_router , args=[]) генерирует url запрос с указаными в нем параметрами
        # "book" к basename нужно добавлять ->
        # -list    если хотим получить список
        # -detail  если хотим получить одну запись
        url = reverse("book-list")  # -> /book/
        # self.client дает APITestCase
        response = self.client.get(
            url
        )  # -> <Response status_code=200, "application/json">
        # возвращает ответ на наш get запрос
        print(
            response.data
        )  # -> [{'id': 1, 'name': 'Test book 1 ', 'price': '25.00'}, {'id': 2, 'name': 'Test book 2 ', 'price': '30.00'}]
