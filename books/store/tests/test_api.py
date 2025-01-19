# Тестируем наш API из django rest

# default django
from django.urls import reverse

# django rest
from rest_framework.test import APITestCase
from rest_framework import status

# my_project
from store.models import Book
from store.serializers import BookSerializer


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

        # BookSerializer([book_1, book_2]) передаем внутрь сериализатора список обьектов
        #  many=True указывает, что передаем список елементов, а не один елемент
        # .data возвращает только данные
        serializer_data = BookSerializer([book_1, book_2], many=True).data
        # status хранит все значения ответов от сервера
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

        # print(response)  # -> <Response status_code=200, "application/json">
        # print(response.data)  # -> [{'id': 1, 'name': 'Test book 1', 'price': '25.00'}, {'id': 2, 'name': 'Test book 2', 'price': '30.00'}]
