# Тестируем наш API из django rest

# default django
from django.urls import reverse
from django.contrib.auth.models import User


# django rest
from rest_framework.test import APITestCase
from rest_framework import status

# my_project
from store.models import Book
from store.serializers import BookSerializer

# addition
import json


class BooksApiTestCase(APITestCase):

    # функция setUp будет запускаться каждый раз перед запуском всех остальных функций ниже
    def setUp(self):
        # создаем одноразового пользователя только для тестирования
        self.user = User.objects.create(username="test_username")

        # добавление атрибутов для созданого класса
        # создание временных полей модели для тестирования выполнения views
        self.book_1 = Book.objects.create(
            name="Test book 1", price="25", author_name="Author 1"
        )
        self.book_2 = Book.objects.create(
            name="Test book 2", price="55", author_name="Author 5"
        )
        self.book_3 = Book.objects.create(
            name="Test book Author 1", price="55", author_name="Author 2"
        )

    # тестируем GET-запрос к серверу
    def test_get(self):

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
        serializer_data = BookSerializer(
            [self.book_1, self.book_2, self.book_3], many=True
        ).data
        # status хранит все значения ответов от сервера
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

        # print(response)  # -> <Response status_code=200, "application/json">
        # print(response.data)  # -> [{'id': 1, 'name': 'Test book 1', 'price': '25.00'}, {'id': 2, 'name': 'Test book 2', 'price': '30.00'}]

    # тестируем выполнение функции фильтрации возвращаемых данных из модели через API
    # тестирование -> /book/?price=500
    def test_filter(self):

        url = reverse("book-list")

        response = self.client.get(
            url, data={"price": 55}
        )  # -> 127.0.0.1:8000/book/?price=500

        serializer_data = BookSerializer([self.book_2, self.book_3], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # тестирование -> book/?search=500
    def test_get_search(self):

        url = reverse("book-list")

        response = self.client.get(
            url, data={"search": "Author 1"}
        )  # -> 127.0.0.1:8000/book/?search=Hemingway

        serializer_data = BookSerializer([self.book_1, self.book_3], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # тестирование POST-запроса, создание одной новой ячейки в базе
    def test_create(self):
        url = reverse("book-list")
        data = {
            "name": "Programming in Python3",
            "price": 150,
            "author_name": "Mark Sumerfield",
        }
        # преобразовываем данные из data в json формат для отправки на сервер
        json_data = json.dumps(data)

        # одноразовая авторизация пользователя только для тестирования
        self.client.force_login(self.user)
        # self.client.post отправляем post-запрос
        # data=json_data передаем сайту данные в json формате
        response = self.client.post(
            url, data=json_data, content_type="application/json"
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
