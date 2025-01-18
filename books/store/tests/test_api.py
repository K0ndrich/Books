# Тестируем наш API из django rest

# default django
from django.urls import reverse

# django rest
from rest_framework.test import APITestCase

# my_project
from store.models import Book


class BooksApiTestCase(APITestCase):
    # тестируем GET-запрос к серверу
    def test_get(self):

        book_1 = Book.objects.create(name="Test book 1", price="25")
        book_2 = Book.objects.create(name="Test book 2", price="30")

        # reverse возвращает целый url-путь по указаному его пути из
        # router.register(r"book", BookViewSet)   или   path('new-path/', views.new_view, name='book'),
        url = reverse(
            "book-list"
        )  # -list возвращет список из елементов, -detail возвращает один елемент
        # print(url)  # -> /book/

        # self.client.get(url) отпраляем get-запрос на сервер и даем етот ответ пользователю
        response = self.client.get(url)

        # print(response)  # -> <Response status_code=200, "application/json">
        # print(response.data)  # -> [{'id': 1, 'name': 'Test book 1', 'price': '25.00'}, {'id': 2, 'name': 'Test book 2', 'price': '30.00'}]
